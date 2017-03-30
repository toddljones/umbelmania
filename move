curl \
    --header "Content-Type:application/json" \
    --data '
           {"gamestate":{"opponent_name":"El Rey Muy Dante","player_name":"relampago engrasado","opponent_moves":["A","B","D","G","K"],"total_score":2,"id":"ca65f60d-5a89-406c-a079-3212321423bc","your_moves":["K","K","K","K","K"],"score":0,"state_id":9,"seed":7996821803495312627,"opponent_move":"K","moves_remaining":995,"email":"toddljones@gmail.com","opponent":"el-rey-muy-dante"},"move":"K","signature":"v2V8y62E6r7xWK2UdQ2Un422R7M="}
           ' \
    https://umbelmania.umbel.com/training/ \
    | tee $0.out


