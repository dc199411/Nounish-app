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
            src="@/assets/images/game/status-gameover.png"
          />
          <p>Room ID: sfasdfa</p>
        </el-col>
        <el-col :span="14">
          <h2 class="Connect-wa">Game Over</h2>
          <p class="wallet-disc">
            As soon as we have enough people in this room, the game begins.
          </p>
          <div class="member-box">Jason.eth</div>
          <div class="member-box"></div>
          <div class="member-box member-box-gray"></div>
          <div class="member-box member-box-gray"></div>
          <div class="member-box member-box-gray"></div>
          <div class="member-box member-box-gray"></div>

          <el-button @click="startgame()" class="deposit-button"
            >Start Game</el-button
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
    startgame() {
      this.$router.push("/game/111/waitroom");
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
