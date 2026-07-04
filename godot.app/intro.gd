extends Node

@onready var start_button = $startbutton
@onready var name_input = $NameInput


func _ready():

	pass

func _on_name_saved():

	get_tree().change_scene_to_file("res://Main.tscn")


func _on_startbutton_pressed() -> void:
	Network.send_name(name_input.text)
	get_tree().change_scene_to_file("res://Main.tscn")
