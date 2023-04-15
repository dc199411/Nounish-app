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
            src="@/assets/images/game/shishistatus/LOADING1.gif"
          />
          <p>Room ID: sfasdfa</p>
        </el-col>
        <el-col :span="14">
          <h2 class="Connect-wa">Waiting to start</h2>
          <p class="wallet-disc">
            As soon as we have enough people in this room, the game begins.
          </p>

          <div v-for="n of 6" :key="n">
            <div v-if="n <= users.length">
              <div class="member-box">{{ users[n - 1].address }}</div>
            </div>
            <div v-if="n > users.length">
              <div class="member-box member-box-gray"></div>
            </div>
          </div>

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
import axios from "axios";
import Web3 from "web3";

export default {
  data() {
    return {
      roomId: this.$route.params.id,
      isReadyToStart: false,
      users: [
        {
          address: "0xafasduhkhaskljhfasdf",
        },
        {
          address: "0x34rsdfu7hkjrfffasfae",
        },
      ],
      myAddress: "",
    };
  },

  async mounted() {
    const MMSDK = new MetaMaskSDK(this.options);
    ethereum = MMSDK.getProvider();
    let instance = new Web3(window.ethereum);
    try {
      window.ethereum.enable();
      web3 = instance;
      web3.eth.getAccounts().then((accounts) => {
        this.myAddress = accounts[0];
      });
    } catch (error) {
      alert("Please allow access for the app to work");
    }
  },

  methods: {
    startgame() {
      axios.post(
        "https://discord.com/api/webhooks/1096937215604555847/PWoHOsYEdzzIOLKnpOe0OJ9ivXI2MJQzl2mwg5Y87VxONMNx8q_6CQlrXOWp46WGi9Iv",
        {
          username: "Game Streamer",
          avatar_url:
            "https://shishiodoshi-app-k22f.vercel.app/_nuxt/img/game-4p-start.f825b8e.png",
          content:
            "😎 gamestart!!! \r https://shishiodoshi-app-k22f.vercel.app/_nuxt/img/game-4p-start.f825b8e.png \r Let's join to the game from link below 😎 \r https://shishiodoshi-app-k22f.vercel.app/game/111/",
        }
      );
      this.$router.push("/game/" + this.roomId + "/ingame");
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
