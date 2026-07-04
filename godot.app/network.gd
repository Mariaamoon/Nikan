extends Node

signal server_ready
signal name_saved
signal quote_received(data)

var health_http: HTTPRequest
var name_http: HTTPRequest
var quote_http: HTTPRequest

var checking_server = false

func _ready():
	health_http = HTTPRequest.new()
	add_child(health_http)
	health_http.request_completed.connect(_on_health_completed)

	name_http = HTTPRequest.new()
	add_child(name_http)
	name_http.request_completed.connect(_on_name_completed)

	quote_http = HTTPRequest.new()
	add_child(quote_http)
	quote_http.request_completed.connect(_on_quote_completed)

	start_server()


func start_server():
	var pid = OS.create_process(
	"C:/Users/jam/AppData/Local/Programs/Python/Python313/python.exe",
	["-m", "uvicorn", "server:app", "--host", "127.0.0.1", "--port", "8000"]
)
	print("Server process PID:", pid)
	await get_tree().create_timer(1).timeout
	check_server()


func check_server():
	checking_server = true
	print("Checking server...")
	health_http.request("http://127.0.0.1:8000/")


func send_name(name):
	if checking_server == true:
		print("Sending name:", name)
		var body = {"name": name}
		var headers = ["Content-Type: application/json"]
		var err = name_http.request(
			"http://127.0.0.1:8000/set_name",
			headers,
			HTTPClient.METHOD_POST,
			JSON.stringify(body)
		)
		print("Request result:", err)


func request_quote(text):
	print("Requesting quote:", text)
	var body = {"text": text}
	var headers = ["Content-Type: application/json"]
	var err = quote_http.request(
		"http://127.0.0.1:8000/recommend",
		headers,
		HTTPClient.METHOD_POST,
		JSON.stringify(body)
	)
	print("Request result:", err)


func _on_health_completed(result, response_code, headers, body):
	print("Health check result:", result, " response code:", response_code)
	if response_code != 200:
		await get_tree().create_timer(1).timeout
		check_server()
		return
	checking_server = false
	emit_signal("server_ready")


func _on_name_completed(result, response_code, headers, body):
	var response = body.get_string_from_utf8()
	print("Result enum:", result)
	print("Response code:", response_code)
	print("Response code:", response_code)
	print("Name response:", response)
	var data = JSON.parse_string(response)
	if data == null:
		return
	if "success" in data:
		emit_signal("name_saved")


func _on_quote_completed(result, response_code, headers, body):
	var response = body.get_string_from_utf8()
	print("Quote response:", response)
	var data = JSON.parse_string(response)
	if data == null:
		return
	emit_signal("quote_received", data)
