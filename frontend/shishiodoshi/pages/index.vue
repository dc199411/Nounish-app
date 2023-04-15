<template>
  <el-container class="container">
    <el-header class="header">
      <el-row>
        <el-col :span="18">
          <img src="images/logo.png" />
        </el-col>
        <el-col :span="3">
          <a href="https://nuxtjs.org/" target="_blank"> Doc</a>
        </el-col>
        <el-col :span="3">
          <img src="images/connect-wallet.png" />
        </el-col>
      </el-row>
    </el-header>
    <el-main class="in-game">
      <!-- <el-row :gutter="84"> -->
      <el-row>
        <el-col :span="10">
          <img src="images/game/game-4p-start.png" />
          <p>Room ID: sfasdfa</p>
        </el-col>
        <el-col :span="14">
          <h2 class="Connect-wa">Connect your wallet to play</h2>
          <p class="wallet-disc">
            Wallets are provided by External Providers and by selecting you
            agree to Terms of those Providers.
          </p>
          <el-row :gutter="14">
            <el-col :span="10">
              <p>Select preferred network:</p>
            </el-col>
            <el-col :span="10">
              <el-select
                v-model="value"
                class="m-2"
                placeholder="Ethareum Mainnet"
                size="large"
              >
                <el-option
                  v-for="item in options"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value"
                />
              </el-select>
            </el-col>
          </el-row>
          <button @click="login_metamask()">login metamask</button>
          <button @click="selected_address()">check address metamask</button>

          <el-row :gutter="10">
            <el-col :span="5">
              <div class="wallet-box" @click="login_metamask()">
                <img src="images/metamask.jpg" />
                <p>Metamask</p>
              </div>
            </el-col>
            <el-col :span="5">
              <div class="wallet-box">
                <img src="images/metamask.jpg" />
                <p>Metamask</p>
              </div>
            </el-col>
            <el-col :span="5">
              <div class="wallet-box">
                <img src="images/metamask.jpg" />
                <p>Metamask</p>
              </div>
            </el-col>
            <el-col :span="5">
              <div class="wallet-box">
                <img src="images/metamask.jpg" />
                <p>Metamask</p>
              </div>
            </el-col>
            <el-col :span="5">
              <div class="wallet-box">
                <img src="images/metamask.jpg" />
                <p>Metamask</p>
              </div>
            </el-col>
            <el-col :span="5">
              <div class="wallet-box">
                <img src="images/metamask.jpg" />
                <p>Metamask</p>
              </div>
            </el-col>
            <el-col :span="5">
              <div class="wallet-box">
                <img src="images/metamask.jpg" />
                <p>Metamask</p>
              </div>
            </el-col>
          </el-row>
        </el-col>
      </el-row>
    </el-main>

    <el-footer class="footer">
      <img src="images/footer.png" />
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
.container {
  margin: 22px 64px;
  display: flex;
}

.header {
  margin-bottom: 114px;
}

.in-game img {
  width: 480px;
}

.wallet-disc {
  margin-bottom: 80px;
}

h2.Connect-wa {
  margin-bottom: 24px;
}
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
</style>
