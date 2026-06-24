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

def show_player(player):
    header = f"{'Mã cầu thủ':<10} | {'Họ tên':<20} | {'Tốc độ':<20} | {'Kỹ thuật':<20} | {'Ghi bàn':<20} | {'Điểm phong độ':<20} | {'Phân loại':<20}"
    print("DANH SÁCH CẦU THỦ")
    print(header)
    print("-"*len(header))

    if len(players) == 0:
        print("Danh sách rỗng")
    else:
        for player in player:
            print(f"{player['id']:<10} | {player['name']:<20} | {player['speed_score']:<20} | {player['technique_score']:<20} | {player['goal_score']:<20} | {player['average_score']:<20} | {player['performance_type']:<20}")


show_player(players)