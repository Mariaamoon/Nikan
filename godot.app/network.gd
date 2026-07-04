extends Node

signal server_ready
signal name_saved
signal quote_received(data)

var health_http : HTTPRequest
var api_http : HTTPRequest

var checking_server = false

func _ready():

	health_http = HTTPRequest.new()
	add_child(health_http)
	health_http.request_completed.connect(_on_health_completed)

	api_http = HTTPRequest.new()
	add_child(api_http)
	api_http.request_completed.connect(_on_api_completed)

	start_server()


func start_server():

	OS.create_process(
	"C:/Users/jam/AppData/Local/Programs/Python/Python313/python.exe",
		 ["-m",
		"uvicorn",
		"server:app",
		"--host", "127.0.0.1",
		"--port", "8000"]
	)

	await get_tree().create_timer(2).timeout

	check_server()


func check_server():

	checking_server = true

	health_http.request(
        "http://127.0.0.1:8000/"
	)


func send_name(name):
	print("Sending name:", name)

	var body = {
		"name": name
	}
	print("JSON:", JSON.stringify(body))

	var headers = [
        "Content-Type: application/json"
	]

	var err = api_http.request(
		"http://127.0.0.1:8000/set_name",
		headers,
		HTTPClient.METHOD_POST,
		JSON.stringify(body)
	)
	print("Request result:", err)

func request_quote(text):
	print("Requesting quote:", text)

	var body = {
		"text": text
	}

	var headers = [
        "Content-Type: application/json"
	]

	api_http.request(
		"http://127.0.0.1:8000/recommend",
		headers,
		HTTPClient.METHOD_POST,
		JSON.stringify(body)
	)


func _on_health_completed(result,response_code,headers,body):

	if response_code != 200:

		await get_tree().create_timer(1).timeout

		check_server()

		return

	emit_signal("server_ready")


func _on_api_completed(result,response_code,headers,body):

	var response = body.get_string_from_utf8()

	print(response)

	var data = JSON.parse_string(response)
	print("API Response:", data)
	if data == null:
		return

	if "success" in data:

		emit_signal("name_saved")

	elif "text" in data:

		emit_signal("quote_received",data)
