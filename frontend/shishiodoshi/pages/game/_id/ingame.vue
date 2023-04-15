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
            src="@/assets/images/game/game-4p-start.png"
          />
          <p>Room ID: sfasdfa</p>
        </el-col>
        <el-col :span="14">
          <h2 class="Connect-wa">Gogo.eth ‘s Turn - 49s</h2>
          <p class="wallet-disc">Choose the number of coins you want to bid</p>
          <div class="game-member-box">
            <div class="member-box">Jason.eth</div>
            <div class="total-score">23</div>
            <div class="add-score"></div>
          </div>

          <div class="game-member-box">
            <div class="member-box">aaa.eth</div>
            <div class="total-score">13</div>
            <div class="add-score"></div>
          </div>
          <div class="member-box member-box-gray"></div>
          <div class="member-box member-box-gray"></div>
          <div class="member-box member-box-gray"></div>
          <div class="member-box member-box-gray"></div>

          <el-button @click="finish()" class="deposit-button"
            >End game</el-button
          >
        </el-col>
      </el-row>
    </el-main>

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
    return {};
  },

  async mounted() {
    // window.$state = this.$store.state;
  },

  methods: {
    finish() {
      this.$router.push("/game/111/result");
    },
    async value() {},
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
