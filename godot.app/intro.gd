extends Node

@onready var start_button = $startbutton
@onready var name_input = $NameInput

var pending_name = ""
var server_is_ready = false

func _ready():
	Network.server_ready.connect(_on_server_ready)
	Network.name_saved.connect(_on_name_saved)
	Network.quote_received.connect(_on_quote_received)

func _on_startbutton_pressed() -> void:
	pending_name = name_input.text
	if server_is_ready:
		Network.send_name(pending_name)
		get_tree().change_scene_to_file("res://Main.tscn")
	else:
		print("Waiting for server to be ready...")

func _on_server_ready():
	server_is_ready = true
	if pending_name != "":
		Network.send_name(pending_name)
		get_tree().change_scene_to_file("res://Main.tscn")

func _on_name_saved():
	print("Name was saved!")

func _on_quote_received(data):
	print("Got quote:", data)
