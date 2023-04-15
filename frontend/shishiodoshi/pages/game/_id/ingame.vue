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
        <el-col :span="10">
          <img
            class="game-status"
            src="@/assets/images/game/game-2p-start.png"
          />
          <p>Room ID: sfasdfa</p>
        </el-col>
        <el-col :span="14">
          <div v-if="currentUserIndex == myAddress"></div>
          <div v-if="currentUserIndex != myAddress">
            <h2 class="Connect-wa">
              {{ users[currentUserIndex].address }} ‘s Turn
            </h2>
            <p class="wallet-disc">
              Choose the number of coins you want to bid
            </p>
            <div v-for="n of 6" :key="n">
              <div v-if="n <= users.length">
                <div class="game-member-box">
                  <div class="member-box">{{ users[n - 1].address }}</div>
                  <div class="total-score">{{ users[n - 1].totalBet }}</div>
                  <div class="add-score"></div>
                </div>
              </div>
              <div v-if="n > users.length">
                <div class="member-box member-box-gray"></div>
              </div>
            </div>
          </div>

          <el-button @click="finish()" class="deposit-button"
            >End game</el-button
          >
        </el-col>
      </el-row>
    </el-main>
    <iframe
      src="https://discord.com/widget?id=1095996892074225695&theme=dark"
      width="350"
      height="500"
      allowtransparency="true"
      frameborder="0"
      sandbox="allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts"
    ></iframe>

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

export default {
  data() {
    return {
      gamestateList: ["start", "ingame", "finish"],
      currentGamestate: "start",
      shishiodoshirisk: [],
      currentTurn: 1,
      users: [
        {
          address: "0xafasduhkhaskljhfasdf",
          totalBet: 0,
        },
        {
          address: "0x34rsdfu7hkjrfffasfae",
          totalBet: 0,
        },
      ],
      myAddress: "sss",
      currentUserIndex: 0,
      currentBetPrice: 0,
      winUserIndex: 0,
      loseUserIndex: 0,
      currentTotalBetPrice: 0,
      maxBet: 0,
      userBets: [0, 0],
      isGameOver: false,
    };
  },

  async mounted() {
    // window.$state = this.$store.state;
  },

  methods: {
    bet() {
      this.currentTotalBetPrice =
        this.currentTotalBetPrice + this.currentBetPrice;

      this.currentTurn = this.currentTurn + 1;
    },
    finish() {
      this.$router.push("/game/111/result");
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
</style>
