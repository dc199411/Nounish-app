<template>
  <el-container class="container">
    <!-- <el-header class="header">
      <el-row class="header-contents">
        <el-col :span="18">
          <img class="logo" src="@/assets/images/logo.png" />
        </el-col>
        <el-col :span="3">
          <p class="doc-link">Doc</p>
        </el-col>
        <el-col :span="3">
          <img src="@/assets/images/connect-wallet.png" />
        </el-col>
      </el-row>
    </el-header> -->
    <el-footer class="header">
      <img src="@/assets/images/header2.png" />
    </el-footer>
    <el-main class="in-game">
      <!-- <el-row :gutter="84"> -->
      <el-row>
        <div v-if="isGameOver">
          <h1>Finish!!</h1>
          <el-col :span="10" style="padding-top: 20px">
            <p class="token-name">Total:</p>
            <p class="total-bet">
              {{ currentTotalBetPrice }} ({{
                (currentTotalBetPrice * 0.1).toPrecision([3])
              }})APE
            </p>
            <img
              style="margin-top: 0px"
              class="game-status"
              src="@/assets/images/game/shishistatus/GIFOVER.gif"
            />
            <p>Room ID: {{ roomId }}</p>
          </el-col>
          <el-col :span="14">
            <h2 class="Connect-wa">Game Over</h2>
            <p class="wallet-disc">
              {{ users[winUserIndex].address.substring(0, 13) }}... wins. <br />
              All tokens bid by
              {{ users[loseUserIndex].address.substring(0, 13) }}... are lost
              and belong to
              {{ users[winUserIndex].address.substring(0, 13) }}....
            </p>

            <div>
              <div v-for="n of 6" :key="n">
                <div v-if="n <= users.length">
                  <div class="game-member-box">
                    <div class="member-box">
                      {{ users[n - 1].address.substring(0, 13) }}...
                    </div>
                    <div class="total-score">{{ users[n - 1].totalBet }}</div>
                    <div class="add-score"></div>
                  </div>
                </div>
                <div v-if="n > users.length">
                  <div class="member-box member-box-gray"></div>
                </div>
              </div>
            </div>
          </el-col>
        </div>
        <div v-if="isGameOver == false">
          <img class="chat-img" src="@/assets/images/game/chat_roop.gif" />
          <el-col :span="10" style="padding-top: 20px">
            <p class="token-name">Total:</p>
            <p class="total-bet">
              <!-- {{ currentTotalBetPrice }} ({{ currentTotalBetPrice * 0.1 }})APE -->
              {{ currentTotalBetPrice }} ({{
                (currentTotalBetPrice * 0.1).toPrecision([3])
              }})APE
            </p>

            <img
              style="margin-top: 0px"
              class="game-status"
              v-if="shishiodoshiriskLevel == 0"
              src="@/assets/images/game/shishistatus/GIF00.gif"
            />
            <img
              style="margin-top: 0px"
              class="game-status"
              v-if="shishiodoshiriskLevel == 1"
              src="@/assets/images/game/shishistatus/GIF01.gif"
            />
            <img
              style="margin-top: 0px"
              class="game-status"
              v-if="shishiodoshiriskLevel == 2"
              src="@/assets/images/game/shishistatus/GIF02.gif"
            />
            <img
              style="margin-top: 0px"
              class="game-status"
              v-if="shishiodoshiriskLevel == 3"
              src="@/assets/images/game/shishistatus/GIF03.gif"
            />
            <img
              style="margin-top: 0px"
              class="game-status"
              v-if="shishiodoshiriskLevel == 4"
              src="@/assets/images/game/shishistatus/GIF04.gif"
            />
            <p>Room ID: {{ roomId }}</p>
          </el-col>
          <el-col :span="14">
            <h2 class="Connect-wa">
              {{ users[currentUserIndex].address.substring(0, 13) }}... ‘s Turn
            </h2>
            <p class="wallet-disc">
              Choose the number of coins you want to bid
            </p>
            <div v-if="users[currentUserIndex].address == myAddress">
              <div>
                <p class="token-name">Token:　</p>
                <button class="allow" @click="sumBet(-1)">＜</button>
                　{{ currentBetPrice }}　
                <button class="allow" @click="sumBet(1)">＞</button>
              </div>
              <img
                class="coin-image"
                v-if="currentBetPrice == 0"
                src="@/assets/images/game/Coin1.png"
              />
              <img
                class="coin-image"
                v-if="currentBetPrice == 1"
                src="@/assets/images/game/Coin1.png"
              />
              <img
                class="coin-image"
                v-if="currentBetPrice == 2"
                src="@/assets/images/game/Coin2.png"
              />
              <img
                class="coin-image"
                v-if="currentBetPrice == 3"
                src="@/assets/images/game/Coin3.png"
              />
              <img
                class="coin-image"
                v-if="currentBetPrice == 4"
                src="@/assets/images/game/Coin4.png"
              />
              <img
                class="coin-image"
                v-if="currentBetPrice == 5"
                src="@/assets/images/game/Coin5.png"
              />
              <img
                class="coin-image"
                v-if="currentBetPrice == 6"
                src="@/assets/images/game/Coin6.png"
              />
              <img
                class="coin-image"
                v-if="currentBetPrice == 7"
                src="@/assets/images/game/Coin7.png"
              />
              <img
                class="coin-image"
                v-if="currentBetPrice == 8"
                src="@/assets/images/game/Coin8.png"
              />
              <img
                class="coin-image"
                v-if="currentBetPrice == 9"
                src="@/assets/images/game/Coin9.png"
              />
              <img
                class="coin-image"
                v-if="currentBetPrice == 10"
                src="@/assets/images/game/Coin10.png"
              />
              <div style="margin-left: 40px">
                <el-button
                  style="float: left"
                  @click="bet()"
                  class="deposit-button"
                  >Bet</el-button
                >
              </div>
            </div>
            <div v-if="users[currentUserIndex].address != myAddress">
              <div v-for="n of 6" :key="n">
                <div v-if="n <= users.length">
                  <div class="game-member-box">
                    <div class="member-box">
                      {{ users[n - 1].address.substring(0, 13) }}...
                    </div>
                    <div class="total-score">{{ users[n - 1].totalBet }}</div>
                    <div class="add-score"></div>
                  </div>
                </div>
                <div v-if="n > users.length">
                  <div class="member-box member-box-gray"></div>
                </div>
              </div>
            </div>

            <!-- <el-button @click="finish()" class="deposit-button"
            >End game</el-button
          > -->
          </el-col>
        </div>
      </el-row>
    </el-main>
    <!-- <iframe
      src="https://discord.com/widget?id=1095996892074225695&theme=dark"
      width="350"
      height="500"
      allowtransparency="true"
      frameborder="0"
      sandbox="allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts"
    ></iframe> -->

    <el-footer class="footer">
      <img src="@/assets/images/footer.png" />
    </el-footer>
  </el-container>
  <!-- <div class="container">
      
    </div> -->
</template>

<script>
// const Cookie = process.client ? require("js-cookie") : undefined;
import MetaMaskSDK from "@metamask/sdk";
import Web3 from "web3";
import axios from "axios";

export default {
  data() {
    return {
      roomId: this.$route.params.id,
      gamestateList: ["start", "ingame", "finish"],
      currentGamestate: "start",
      shishiodoshiriskLevel: 0,
      currentTurn: 1,
      users: [
        {
          address: "0xBdAAa850F1345b6f1936ee7cb30D63C07eEBD",
          totalBet: 0,
        },
        {
          address: "0x0277fE8E6D9b07d20B20a7922115431f183e33",
          totalBet: 0,
        },
      ],
      myAddress: "",
      currentUserIndex: 0,
      currentBetPrice: 1,
      coinImagePath:
        '"@/assets/images/game/Coin' + this.currentBetPrice + '.png"',
      winUserIndex: 0,
      loseUserIndex: 0,
      currentTotalBetPrice: 0,
      maxBet: 20,
      userBets: [0, 0],
      isGameOver: false,
      bgm: new Audio("@/assets/sound/BGM.mp3"),
      betSound: new Audio("@/assets/sound/Bid.mp3"),
      GameoverSound: new Audio("@/assets/sound/Gameover.mp3"),
      turnchangeSound: new Audio("@/assets/sound/YourTurn.mp3"),
    };
  },

  async beforeCreate() {
    const MMSDK = new MetaMaskSDK(this.options);
    ethereum = MMSDK.getProvider();
    let instance = new Web3(window.ethereum);
    try {
      window.ethereum.enable();
      web3 = instance;
      web3.eth.getAccounts().then((accounts) => {
        this.myAddress = accounts[0];
        this.users[0].address = this.myAddress;
      });
    } catch (error) {
      alert("Please allow access for the app to work");
    }
  },

  async mounted() {
    this.maxBet = Math.floor(Math.random() * 40) + 10;
    var self = this;
    setInterval(function () {
      self.updateStatus();
    }, 7000);
    // this.bgm.play();
  },

  methods: {
    bet() {
      // this.betSound.play();
      this.currentTotalBetPrice =
        this.currentTotalBetPrice + this.currentBetPrice;
      this.users[this.currentUserIndex].totalBet =
        this.users[this.currentUserIndex].totalBet + this.currentBetPrice;

      if (this.users[this.currentUserIndex].totalBet > this.maxBet) {
        this.gameOver();
        return;
      }

      this.currentTurn = this.currentTurn + 1;
      this.currentBetPrice = 1;
      this.changeTurn();

      axios.post(
        "https://discord.com/api/webhooks/1096937215604555847/PWoHOsYEdzzIOLKnpOe0OJ9ivXI2MJQzl2mwg5Y87VxONMNx8q_6CQlrXOWp46WGi9Iv",
        {
          username: "Game Streamer",
          avatar_url:
            "https://shishiodoshi-app-k22f.vercel.app/_nuxt/img/game-4p-start.f825b8e.png",
          content:
            this.users[this.currentUserIndex].address +
            " bet " +
            this.currentBetPrice +
            " coin!! \r https://shishiodoshi-app-k22f.vercel.app/_nuxt/img/GIF0" +
            this.shishiodoshiriskLevel +
            ".gif",
        }
      );
    },
    gameOver() {
      this.loseUserIndex = this.currentUserIndex;
      if (this.loseUserIndex == 0) {
        this.winUserIndex = 1;
      } else {
        this.winUserIndex = 0;
      }
      // this.GameoverSound.play();
      this.isGameOver = true;
    },
    sumBet(val) {
      console.log(val);
      if (this.currentBetPrice == 1 && val < 0) {
        return;
      }
      if (this.currentBetPrice == 10 && val > 0) {
        return;
      }
      this.currentBetPrice = this.currentBetPrice + val;
    },
    updateStatus() {
      // this.users = [
      //   {
      //     address: "0xBdAAa850Fea91345b6f1936ee7cb30D63C07eEBD",
      //     totalBet: 0,
      //   },
      //   {
      //     address: "0x0277fE8E6D9b0C47d20B20a7922115431f183e33",
      //     totalBet: 0,
      //   },
      // ];
      if (this.users[this.currentUserIndex].address == this.myAddress) {
        return;
      }
      this.currentBetPrice = Math.floor(Math.random() * 7) + 2;

      this.shishiodoshiriskLevel =
        Math.floor(this.currentTotalBetPrice / (this.maxBet * 2)) + 1;
      this.bet();
    },
    changeTurn() {
      if (this.currentUserIndex == 1) {
        this.currentUserIndex = 0;
      } else {
        this.currentUserIndex = 1;
      }
    },
    finish() {
      this.$router.push("/game/" + this.roomId + "/result");
    },
    async login_metamask() {
      const options = {
        injectProvider: false,
        communicationLayerPreference: "webrtc",
      };
      const MMSDK = new MetaMaskSDK(options);
      const ethereum = MMSDK.getProvider();
      ethereum.request({ method: "eth_requestAccounts", params: [] });
    },
    async selected_address() {
      const options = {
        injectProvider: false,
        communicationLayerPreference: "webrtc",
      };
      const MMSDK = new MetaMaskSDK(options);
      const ethereum = MMSDK.getProvider();
      ethereum.request({ method: "eth_selectedAddress", params: [] });
    },
  },
};
</script>

<style>
.wallet-box {
  height: 120px;
  margin-bottom: 24px;
  text-align: center;
  border: solid 3px #51cc7b;
  border-radius: 24px 24px;
}
.wallet-box img {
  width: 60px;
  display: block;
  margin: 0 auto;
  margin-top: 14px;
}

.footer {
  margin-top: 150px;
}

.footer img {
  width: 100%;
}

.room-info-column {
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 36px;
}

.room-info-column .title {
  display: inline;
}

.room-info-column .value {
  display: inline;
  color: #51cc7b;
}

.deposit-button {
  font-size: 24px;
  font-weight: bold;
  color: #fff;
  height: 60px;
  width: 168px;
  background-color: #51cc7b;
  /* float: right; */
  border-radius: 24px 24px;
}

.doc-link {
  font-size: 18px;
  font-weight: bold;
}

.header-contents {
  display: flex;
  align-items: center;
}

.game-member-box {
  display: flex;
}

.member-box {
}
.total-score {
  font-weight: bold;
  width: 48px;
  height: 48px;
  display: flex;
  border: 3px solid #000000;
  border-radius: 24px;
  align-items: center;
  justify-content: center;
  margin-left: 8px;
}
.add-score {
  margin-left: 8px;
  width: 48px;
  height: 48px;
  align-items: center;
  justify-content: center;
  margin-left: 8px;
  color: #51cc7b;
}

.member-box {
  height: 48px;
  width: 240px;
  box-sizing: border-box;
  border: 3px solid #000000;
  border-radius: 24px;
  margin-bottom: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 18px;
}

.member-box-gray {
  border: 3px solid #c0c0c0;
}

.allow {
  font-size: 24px;
  color: #51cc7b;
}

.token-name {
  font-size: 24px;
  font-weight: bold;
  display: inline;
}

.total-bet {
  font-size: 24px;
  font-weight: bold;
  color: #51cc7b;
  display: inline;
}

.coin-image {
  width: 216px;
  margin-left: 30px;
}

.chat-img {
  position: fixed;
  right: 0;
  top: 0;
  width: 480px;
}
</style>
