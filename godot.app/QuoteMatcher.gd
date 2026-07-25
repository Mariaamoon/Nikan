extends Node

var quotes_data: Array = []
var intro_templates: Array = [
	"I hear you. When things feel that way, I find comfort in this thought:",
	"Thank you for opening up. Here is a quote that might offer some perspective:",
	"I completely understand. Take a moment with this:",
	"That is totally valid. Keep this reflection in mind today:"
]

func _ready():
	load_quotes_data()

# 1. Load quotes and pre-computed embeddings from JSON
func load_quotes_data():
	var file_path = "res://quotes_data.json"
	if FileAccess.file_exists(file_path):
		var file = FileAccess.open(file_path, FileAccess.READ)
		var json_text = file.get_as_text()
		quotes_data = JSON.parse_string(json_text)
		print("✅ Loaded ", quotes_data.size(), " quotes into Godot memory.")
	else:
		push_error("Could not find res://quotes_data.json!")

# 2. Math Utility: Cosine Similarity between two Array[float] vectors
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

# 3. Match User Input Vector against Quote Database
func find_best_quote(user_vector: Array) -> Dictionary:
	var best_score: float = -1.0
	var best_quote: Dictionary = {}
	
	for item in quotes_data:
		var quote_vector = item["embedding"]
		var score = calculate_cosine_similarity(user_vector, quote_vector)
		
		if score > best_score:
			best_score = score
			best_quote = item
			
	return {"quote": best_quote.get("text", ""), "score": best_score}

# 4. Generate full conversational response
func get_chat_response(user_name: String, user_vector: Array) -> String:
	var result = find_best_quote(user_vector)
	var matched_text = result["quote"]
	
	var intro = intro_templates[randi() % intro_templates.size()]
	return "Hey " + user_name + "! " + intro + "\n\n👉 \"" + matched_text + "\""
