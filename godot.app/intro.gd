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
	Network.send_name(name_input.text)
	get_tree().change_scene_to_file("res://Main.tscn")
