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
    * [24]: Trên bàn còn bài để bốc không (0,1).
    * [25: 28]: Thông tin về PHASE của người chơi:
        - 0: Bốc
        - 1: Chọn người chơi khác để yêu cầu
        - 2: Chọn lá bài muốn yêu cầu
    * [28: 31]: Người bị yêu cầu.
    * [31]: Game đã kết thúc hay chưa (1 là kết thúc rồi).
