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

@onready var speech = $SpeechBubble/speech
@onready var pages_input = $PagesInput
@onready var pages_label = $PagesLabel
@onready var rank_label = $RankLabel
@onready var xp_bar = $XPBar
@onready var xp_label = $XPLabel
@onready var timer_input = $TimerInput
@onready var timer_label = $TimerLabel
@onready var reading_timer = $ReadingTimer

func _ready():
	load_game()
	update_ui()

func update_ui():

	xp_bar.value = xp
	xp_label.text = "Int: " + str(xp)
	pages_label.text = "Pages Read: " + str(total_pages)
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
	if timer_input.text.is_empty():
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
	reading = false
	var earned_xp = int(timer_input.text)
	add_xp(earned_xp)
	timer_label.text = "Finished!"
	speech.text = "Great job reading!"

func save_game():

	var data = {
		"xp": xp,
		"pages": total_pages
	}
	var file = FileAccess.open(
		"user://save.json",
		FileAccess.WRITE
	)
	file.store_string(
		JSON.stringify(data)
	)

func _on_log_pages_button_pressed():

	if pages_input.text.is_empty():
		return
	var pages = int(pages_input.text)
	total_pages += pages
	add_xp(pages / 2)
	pages_input.clear()
	update_ui()
	save_game()
	speech.text = "\n Nice! You read %d pages!" % pages

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
	update_ui()
