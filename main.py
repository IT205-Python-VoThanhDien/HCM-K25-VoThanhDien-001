from abc import ABC, abstractmethod

class Player(ABC):
    def __init__(self, id, name, speed_score, technique_score, goal_score, average_score, performance_type):
        self.id = id
        self.name = name
        self.speed_score = speed_score
        self.technique_score = technique_score
        self.goal_score = goal_score
        self.average_score = average_score
        self.performance_type = performance_type
    
    @abstractmethod
    def calculate_average(self):
        return float(self.speed_score * 0.3 + self.technique_score * 0.4 + self.goal_score * 0.3)
    
    @abstractmethod
    def classify_performance(self):
        pass

class PlayerManager(ABC):
    def __init__(self):
        self.player = [
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

    def add_player(self):
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
            "average_score": 9,
            "performance_type": "Goat"
        }

        self.player.append(new_player)
        print("Đã thêm cầu thủ thành công")
    
    def show_all(self):
        header = f"{'Mã cầu thủ':<10} | {'Họ tên':<20} | {'Tốc độ':<20} | {'Kỹ thuật':<20} | {'Ghi bàn':<20} | {'Điểm phong độ':<20} | {'Phân loại':<20}"
        print("DANH SÁCH CẦU THỦ")
        print(header)
        print("-"*len(header))

        if len(self.player) == 0:
            print("Danh sách rỗng")
        else:
            for player in self.player:
                print(f"{player['id']:<10} | {player['name']:<20} | {player['speed_score']:<20} | {player['technique_score']:<20} | {player['goal_score']:<20} | {player['average_score']:<20} | {player['performance_type']:<20}")

    def update_player(self):
        search_id = int(input("Nhập mã cầu thủ cần cập nhật: "))
        for player in self.player:
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

    def delete_player(self):
        search_id = int(input("Nhập mã cầu thủ cần xóa: "))
        for player in self.player:
            if search_id == player["id"]:
                confirm = input("Bạn có chắc chắc muốn xóa cầu thủ này không? (Y/N): ")
                if confirm == 'Y' or confirm == 'y':
                    self.player.remove(player)
                elif confirm == 'N' or confirm == 'n':
                    print("Đã hủy thao tác")
                    break
                else:
                    print("Nhập chưa đúng")

    def search_player(self):
        search_id = int(input("Nhập mã cầu thủ cần xóa: "))
        for player in self.player:
            if search_id == player["id"]:
                self.show_all(player["id"])
            else:
                print("Không tìm thấy cầu thủ")

def main():
    while True:
        print("=============== MENU ===============")
        print("1. Hiển thị danh sách cầu thủ")
        print("2. Thêm cầu thủ mới")
        print("3. Cập nhật thông tin cầu thủ")
        print("4. Xóa cầu thủ")
        print("5. Tìm kiếm cầu thủ")
        print("6. Thoát")
        print("="*50)

        choice = input("Nhập lựa chọn của bạn: ")
        match choice:
            case '1':
                player_manager = PlayerManager()
                player_manager.show_all()
            case '2':
                player_manager = PlayerManager()
                player_manager.add_player()
            case '3':
                player_manager = PlayerManager()
                player_manager.update_player()
            case '4':
                player_manager = PlayerManager()
                player_manager.delete_player()
            case '5':
                player_manager = PlayerManager()
                player_manager.search_player()
            case '6':
                print("Cảm ơn bạn đã sử dụng chương trình")
                break
            case _:
                print("Lựa chọn không hợp lệ vui lòng nhập lại")

main()
            
        
    