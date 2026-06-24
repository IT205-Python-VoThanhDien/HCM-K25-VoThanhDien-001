players = [
    {
        "id": 123,
        "name": "Cristiano Ronaldo",
        "speed_score": 9.9,
        "technique_score": 9.9,
        "goal_score": 9.9,
        "average_score": 9.9,
        "performance_type": "Goat"
    }

]

new_id = input("Nhập mã cầu thủ: ")
new_name = input("Nhập tên cầu thủ: ")
new_speed_score = input("Nhập điểm tốc độ: ")
new_technique_score = input("Nhập điểm kĩ thuật: ")
new_goal_score = input("Nhập điểm ghi bàn: ")

new_player = {
    "id": new_id,
    "name": new_name,
    "speed_score": new_speed_score,
    "technique_score": new_speed_score,
    "goal_score": new_goal_score,
    "average_score": 9.9,
    "performance_type": "Goat"
}

players.append(new_player)

