extends Node

@onready var name_input = $NameInput
@onready var welcome = $welcome

func _ready() -> void:
	welcome.text = "congratulation for becomng a better person!"
func _on_startbutton_pressed():
	if name_input.text.strip_edges() == "":
		return
	Global.player_name = name_input.text
	get_tree().change_scene_to_file("res://main.tscn")
