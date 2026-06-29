shader_type canvas_item;

uniform vec4 color_a : source_color = vec4(0.953, 0.651, 0.878, 1.0); // pink
uniform vec4 color_b : source_color = vec4(0.663, 0.561, 0.941, 1.0); // purple
uniform vec4 color_c : source_color = vec4(0.682, 0.890, 0.969, 1.0); // blue
uniform float speed : hint_range(0.01, 1.0) = 0.08;

void fragment() {
    vec2 uv = UV;
    float t = TIME * speed;

    float wave = sin(uv.x * 3.0 + t * 6.28) * 0.5 + 0.5;
    float mixAmount = sin(t * 6.28 + uv.y * 2.0) * 0.5 + 0.5;

    vec4 colorMix1 = mix(color_a, color_b, uv.x + wave * 0.3);
    vec4 finalColor = mix(colorMix1, color_c, mixAmount);

    COLOR = finalColor;
}