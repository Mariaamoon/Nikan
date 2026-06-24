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
var book_titles= []

@onready var input = $LineEdit
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
	update_ui()

func update_ui():

	xp_bar.value = xp
	xp_label.text = "Int: " + str(xp)
	pages_label.text = "Pages Read: " + str(total_pages)
	book_finished.text = "Books Read: "+ str(books_finished)

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
	time_left = minutes 
	reading = true
	speech.text = "Let's read together!"

func _process(delta):

	if reading:
		time_left -= delta
		var minutes = int(time_left) / 60
		var seconds = int(time_left) 
		timer_label.text = "%02d:%02d" % [minutes, seconds]
		if time_left <= 0:
			finish_reading()

func finish_reading():
	timer_input.clear()
	reading = false
	var earned_xp = int(timer_input.text)
	add_xp(earned_xp)
	timer_label.text = "Finished!"
	speech.text = "Great job reading!"

func save_game():

	var data = {
		"xp": xp,
		"pages": total_pages,
		"books_finished": books_finished,
		"book_titles": book_titles
	}
	var file = FileAccess.open(
		"user://save.json",
		FileAccess.WRITE
	)
	file.store_string(
		JSON.stringify(data)
	)



func load_game():

	if !FileAccess.file_exists("user://save.json"):
		return
	var file = FileAccess.open(
		"user://save.json",
		FileAccess.READ
	)
	var data = JSON.parse_string(
		file.get_as_text()
	)
	if data:
		xp = data.get("xp", 0)
		total_pages = data.get("pages", 0)
		books_finished = data.get("books_finished" ,0)
		book_titles = data.get("book_tites" ,[])
	update_ui()

func add_book_to_shelf(title):
	var label = Label.new()
	label.text = "📕"
	book_titles.append(title)
	book_finished.text = "books finished: %d " % books_finished
	$Bookshelf.add_child(label)

func _on_finish_book_button_pressed() -> void:
	if book_title.text.is_empty() or is_blank(book_title.text):
		return
	add_book_to_shelf(book_title)
	var book = str(book_title.text)
	books_finished += 1
	add_xp(10)
	book_title.clear()
	update_ui()
	save_game()
	speech.text = "\n Nice! You read %s!" % book
	
func is_blank(input:String) -> bool:
	return input.strip_edges().is_empty()

func valid_int(new_text: String):
		var filtered := ""
		for c in new_text:
			if c>= "0" and c<="9":
				filtered+=c
		if new_text != filtered:
			return false
		return true


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
		speech.text = "oops you read nothing today :("
	else:
		speech.text = "\n Nice! You read %d pages!" % pages


func _on_exitbutton_pressed() -> void:
	get_tree().quit()


#func _on_http_request_request_completed(result: int, response_code: int, headers: PackedStringArray, body: PackedByteArray) -> void:
	#var text =body.get_string_from_utf8()
	#var data = JSON.parse_string(text)
	#quote_label.text = data["text"]
func _on_http_request_request_completed(result, response_code, headers, body):
	var response = body.get_string_from_utf8()
	print(response)
	var data = JSON.parse_string(response)
	quote_label.text = data["received"]

func _on_quote_pressed() -> void:
	#http.request( "http://127.0.0.1:8000/quote")
	
	var body = {
	"text": input.text }


	http.request(
		"http://127.0.0.1:8000/recommend",
		["Content-Type: application/json"],
		HTTPClient.METHOD_POST,
		JSON.stringify(body)
	)
