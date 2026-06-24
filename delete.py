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

search_id = int(input("Nhập mã cầu thủ cần xóa: "))
for player in players:
    if search_id == player["id"]:
        confirm = input("Bạn có chắc chắc muốn xóa cầu thủ này không? (Y/N): ")
        if confirm == 'Y' or confirm == 'y':
            players.remove(player)
        elif confirm == 'N' or confirm == 'n':
            print("Đã hủy thao tác")
            break
        else:
            print("Nhập chưa đúng")

        


