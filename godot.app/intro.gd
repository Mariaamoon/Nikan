extends Node

@onready var name_input = $NameInput
@onready var welcome = $welcome
@onready var http = $HTTPRequest

func start_server():
	OS.create_process(
		 "C:/Users/jam/AppData/Local/Programs/Python/Python313/python.exe",
		 ["C:/Users/jam/Documents/nikan/server.py"]
	)

func check_server():
	var err = http.request(
		"http://127.0.0.1:8000/"
	)
	if err != OK:
		await get_tree().create_timer(1).timeout

func _on_http_request_request_completed(result, response_code, headers, body):
	if response_code != 200:
		await get_tree().create_timer(1).timeout
		check_server()
		return

func _ready() -> void:
	welcome.text = "congratulation for becomng a better person!"
func _on_startbutton_pressed():
	if name_input.text.strip_edges() == "":
		return
	Global.player_name = name_input.text
	var body = {
	"name": $NameInput.text
	}
	var headers = [
	"Content-Type: application/json"]
	http.request(
		"http://127.0.0.1:8000/set_name",
		headers,
		HTTPClient.METHOD_POST,
		JSON.stringify(body)
	)
	get_tree().change_scene_to_file("res://main.tscn")
