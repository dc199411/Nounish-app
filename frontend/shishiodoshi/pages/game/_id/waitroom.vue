<template>
  <el-container class="container">
    <el-header class="header">
      <el-row class="header-contents">
        <el-col :span="18">
          <img src="@/assets/images/logo.png" />
        </el-col>
        <el-col :span="3">
          <p class="doc-link">Doc</p>
        </el-col>
        <el-col :span="3">
          <img src="@/assets/images/connect-wallet.png" />
        </el-col>
      </el-row>
    </el-header>
    <el-main class="in-game">
      <!-- <el-row :gutter="84"> -->
      <el-row>
        <el-col :span="10">
          <img src="@/assets/images/game/game-4p-start.png" />
          <p>Room ID: sfasdfa</p>
        </el-col>
        <el-col :span="14">
          <h2 class="Connect-wa">Deposit and join this game</h2>
          <p class="wallet-disc">
            Completion of Deposit is considered your game ready.
          </p>
          <div class="room-info-column">
            <p class="title">Room ID:</p>
            <p class="value">uR8YFsKg</p>
          </div>
          <div class="room-info-column">
            <p class="title">Player:</p>
            <p class="value">4</p>
          </div>
          <div class="room-info-column">
            <p class="title">Token:</p>
            <p class="value">APE</p>
          </div>
          <div class="room-info-column">
            <p class="title">Bid Increment::</p>
            <p class="value">0.1</p>
          </div>
          <div class="room-info-column">
            <p class="title">Minimum Deposit::</p>
            <p class="value">60</p>
          </div>
          <el-button class="deposit-button">Deposit</el-button>
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
    return {
      options: [
        {
          value: "Ethareum Mainnet",
          label: "Ethareum Mainnet",
        },
        {
          value: "Option2",
          label: "Option2",
        },
        {
          value: "Option3",
          label: "Option3",
        },
        {
          value: "Option4",
          label: "Option4",
        },
        {
          value: "Option5",
          label: "Option5",
        },
      ],
    };
  },

  async mounted() {
    // window.$state = this.$store.state;
  },

  methods: {
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
  float: right;
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
</style>
