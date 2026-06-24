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

search_id = int(input("Nhập mã cầu thủ cần cập nhật: "))
for player in players:
    if search_id == player['id']:
        new_speed = input("Nhập tốc độ mới: ")
        new_technique = input("Nhập kĩ thuật mới: ")
        new_goal = input("Nhập điểm ghi bàn mới: ")
        
        player['speed_score'] = new_speed
        player['technique_score'] = new_technique
        player['goal_score'] = new_goal

        print("Đã cập nhật thành công")
        break
else:
    print("Không tìm thấy cầu thủ")


print(players)