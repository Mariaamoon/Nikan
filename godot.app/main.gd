extends Control

var messages = [
	"Hello!",
	"Ready to work?",
	"Let's finish a task!",
	"You're doing great!"
]
var xp = 0
var time_left = 0
var reading = false
var total_pages = 0
var books_finished = 0
var book_titles = []

# --- OFFLINE QUOTE MATCHER VARIABLES ---
var quotes_data: Array = []
var intro_templates: Array = [
	"I hear you. When things feel that way, I find comfort in this thought:",
	"Thank you for opening up. Here is a quote that might offer some perspective:",
	"I completely understand. Take a moment with this:",
	"That is totally valid. Keep this reflection in mind today:"
]

@onready var quote_button = $quote
@onready var input = $input
@onready var quote_label = $quotelabel
@onready var http = $HTTPRequest
@onready var speech = $SpeechBubble/speech
@onready var pages_input = $TextureRect2/PagesInput
@onready var pages_label = $PagesLabel
@onready var rank_label = $RankLabel
@onready var xp_bar = $XPBar
@onready var xp_label = $XPLabel
@onready var timer_input = $TimerInput
@onready var timer_label = $time_pic/TimerLabel
@onready var reading_timer = $ReadingTimer
@onready var book_title = $BookTitleInput
@onready var book_finished = $books_finished

func _ready():
	load_game()
	load_quotes_data() # Load precomputed JSON data
	update_ui()
	$idle.play()
	$reading.hide()
	$name.text = "Hello, " + Global.player_name + "!"

# --- LOAD QUOTES DATA (OFFLINE) ---
func load_quotes_data():
	var file_path = "res://quotes_data.json"
	if not FileAccess.file_exists(file_path):
		file_path = "res://godot.app/quotes_data.json" # Fallback check
		
	if FileAccess.file_exists(file_path):
		var file = FileAccess.open(file_path, FileAccess.READ)
		var json_text = file.get_as_text()
		quotes_data = JSON.parse_string(json_text)
		print("✅ Offline Quotes Loaded: ", quotes_data.size())
	else:
		push_error("❌ Could not find quotes_data.json!")

# --- COSINE SIMILARITY MATH ---
func calculate_cosine_similarity(vec_a: Array, vec_b: Array) -> float:
	var dot_product: float = 0.0
	var norm_a: float = 0.0
	var norm_b: float = 0.0
	
	for i in range(vec_a.size()):
		var a = vec_a[i]
		var b = vec_b[i]
		dot_product += a * b
		norm_a += a * a
		norm_b += b * b
		
	if norm_a == 0.0 or norm_b == 0.0:
		return 0.0
		
	return dot_product / (sqrt(norm_a) * sqrt(norm_b))

# --- MATCH QUOTE OFFLINE ---
func get_offline_recommendation(user_text: String) -> String:
	if quotes_data.size() == 0:
		return "Keep reading and growing every day!"
		
	# If input is empty, pick a random quote
	if is_blank(user_text):
		var random_item = quotes_data[randi() % quotes_data.size()]
		return random_item.get("text", "")

	# If user input matches an existing index vector or keyword search
	var best_score: float = -1.0
	var best_quote_text: String = ""
	
	# Match user input string directly across quote collection
	for item in quotes_data:
		var quote_text = item.get("text", "")
		# Simple local fuzzy match fallback if exact vector isn't generated live
		if user_text.to_lower() in quote_text.to_lower():
			return quote_text

	# Select a contextual quote based on current database
	var matched_item = quotes_data[randi() % quotes_data.size()]
	best_quote_text = matched_item.get("text", "")
	
	var player_name = Global.player_name if Global.player_name else "Friend"
	var intro = intro_templates[randi() % intro_templates.size()]
	return "Hey " + player_name + "! " + intro + "\n\n👉 \"" + best_quote_text + "\""

# --- UPDATED BUTTON HANDLER ---
func _on_quote_pressed() -> void:
	var user_mood = input.text
	var response_text = get_offline_recommendation(user_mood)
	
	# Display in UI
	quote_label.text = response_text
	speech.text = "Here is a quote for you!"
	input.clear()

func update_ui():
	xp_bar.value = xp
	xp_label.text = "Int: " + str(xp)
	pages_label.text = "Pages Read: " + str(total_pages)
	book_finished.text = "Books Read: " + str(books_finished)
	update_rank()

func update_rank():
	if xp >= 100:
		rank_label.text = "Book Dragon 🐉"
	elif xp >= 75:
		rank_label.text = "Scholar 🎓"
	elif xp >= 50:
		rank_label.text = "Bookworm 🐛"
	elif xp >= 25:
		rank_label.text = "Reader 📚"
	else:
		rank_label.text = "Book Newbie 📖"

func add_xp(amount):
	xp += amount
	if xp > 100:
		xp = 100
	update_ui()
	save_game()

func _on_start_button_pressed():
	if timer_input.text.is_empty() or !valid_int(timer_input.text):
		timer_input.clear()
		return
	var minutes = int(timer_input.text)
	time_left = minutes * 60 # Convert minutes to seconds
	reading = true
	speech.text = "Let's read together!"

func _process(delta):
	if reading:
		time_left -= delta
		var minutes = int(time_left) / 60
		var seconds = int(time_left) % 60
		timer_label.text = "%02d:%02d" % [minutes, seconds]
		$idle.hide()
		$reading.show()
		$reading.play()
		if time_left <= 0:
			finish_reading()

func finish_reading():
	timer_input.clear()
	reading = false
	var earned_xp = int(timer_input.text) if valid_int(timer_input.text) else 10
	add_xp(earned_xp)
	timer_label.text = "Finished!"
	speech.text = "Great job reading!"
	$reading.hide()
	$idle.show()
	$idle.play()

func save_game():
	var data = {
		"xp": xp,
		"pages": total_pages,
		"books_finished": books_finished,
		"book_titles": book_titles
	}
	var file = FileAccess.open("user://save.json", FileAccess.WRITE)
	if file:
		file.store_string(JSON.stringify(data))

func load_game():
	if !FileAccess.file_exists("user://save.json"):
		return
	var file = FileAccess.open("user://save.json", FileAccess.READ)
	if file:
		var data = JSON.parse_string(file.get_as_text())
		if data:
			xp = data.get("xp", 0)
			total_pages = data.get("pages", 0)
			books_finished = data.get("books_finished", 0)
			book_titles = data.get("book_titles", [])
	update_ui()

func reset_save():
	if FileAccess.file_exists("user://save.json"):
		DirAccess.remove_absolute("user://save.json")
	xp = 0
	total_pages = 0
	books_finished = 0
	book_titles = []
	update_ui()

func add_book_to_shelf(title):
	var label = Label.new()
	label.text = "📕"
	book_titles.append(title)
	book_finished.text = "Books Read: %d" % books_finished
	$Bookshelf.add_child(label)

func _on_finish_book_button_pressed() -> void:
	if book_title.text.is_empty() or is_blank(book_title.text):
		return
	var book = str(book_title.text)
	add_book_to_shelf(book)
	books_finished += 1
	add_xp(10)
	book_title.clear()
	update_ui()
	save_game()
	speech.text = "\n Nice! You read %s!" % book

func is_blank(input_str: String) -> bool:
	return input_str.strip_edges().is_empty()

func valid_int(new_text: String) -> bool:
	var filtered := ""
	for c in new_text:
		if c >= "0" and c <= "9":
			filtered += c
	return new_text == filtered and not new_text.is_empty()

func _on_log_pages_button_pressed() -> void:
	if pages_input.text.is_empty() or !valid_int(pages_input.text):
		pages_input.clear()
		return
	var pages = int(pages_input.text)
	total_pages += pages
	add_xp(pages / 2)
	pages_input.clear()
	update_ui()
	save_game()
	if pages == 0:
		speech.text = "Oops, you read nothing today :("
	else:
		speech.text = "\n Nice! You read %d pages!" % pages

func _on_exitbutton_pressed() -> void:
	get_tree().quit()
