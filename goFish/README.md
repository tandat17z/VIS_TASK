##  Thông tin quan trọng
    13: Điểm của bản thân
    16, 19, 22: Điểm của người chơi khác
    
## :video_game: Action
    * [0]: Bốc 1 lá từ bộ bài.
    * [1:4]: Chọn người chơi khác (là người bị yêu cầu).
    * [4: 17]: Chọn lá bài yêu cầu ( lá bài = action - 4). ví dụ: Muốn yêu cầu lá số 0 thì là action 4, 
    
## :bust_in_silhouette: P_state
    * [0:13]: Những lá bài của bản thân. Số lượng lá số k = state[k]
    * [13: 15]: Số lượng lá trên tay và số điểm của bản thân.
    * [15 + i*3: 18 + i*3], i = 0, 1, 2: Thông tin của người chơi khác: Số lá trên tay, số điểm, lá bài cao nhất trong bộ 4.
    * [24]: Trên bàn còn bài để bốc không ( 1 là còn).
    * [25: 28]: Thông tin về PHASE của người chơi:
        - 0: Bốc
        - 1: Chọn người chơi khác để yêu cầu
        - 2: Chọn lá bài muốn yêu cầu
    * [28: 31]: Người bị yêu cầu.
    * [31]: Game đã kết thúc hay chưa (1 là kết thúc rồi).
## :globe_with_meridians: ENV_state
    * [0: 52]: Thứ tự các lá trên bộ bài
    * [52]: Số lá còn lại trên bộ bài bốc ---> Lá bài trên cùng để bốc = env[ 52 - env[52]]
    * [53 + i*15: 68 + i*15]: Thông tin của các người chơi:
        - [0: 13]: Những lá bài của người chơi.
        - [13: 15]: Số lượng lá trên tay và số điểm.
    * [113]: turn
    * [114]: phase ( có 4 phase: 0 là bốc, 1 là chọn người bị yêu cầu, 2 là chọn lá bài yêu cầu, 3 là chuyển sang người chơi khác)
    * [115]: người đang bị yêu cầu ( 0 là không có ai, 1-3 )
    * [116]: Lá bài yêu cầu (-1 là không yêu cầu lá nào, 0-12)
    * [117]: EndGame
    
# Luật bổ sung **(để tìm ra người thắng duy nhất)**
    Khi những người chơi bằng điểm nhau thì người có bộ cao nhất sẽ là người chiến thắng.
