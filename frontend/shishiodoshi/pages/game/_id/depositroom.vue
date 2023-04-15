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
          <h2 class="Connect-wa">Deposit and join this game</h2>
          <p class="wallet-disc">
            Completion of Deposit is considered your game ready.
          </p>
          <div class="room-info-column">
            <p class="title">Room ID:</p>
            <p class="value">{{ roomId }}</p>
          </div>
          <div class="room-info-column">
            <p class="title">Player:</p>
            <p class="value">{{ playerCount }}</p>
          </div>
          <div class="room-info-column">
            <p class="title">Token:</p>
            <p class="value">{{ tokenName }}</p>
          </div>
          <div class="room-info-column">
            <p class="title">Bid Increment:</p>
            <p class="value">{{ bidIncrement }}</p>
          </div>
          <div class="room-info-column">
            <p class="title">Minimum Deposit:</p>
            <p class="value">{{ minimumDeposit }}</p>
          </div>
          <el-button @click="startgame" class="deposit-button"
            >Deposit</el-button
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
import Web3 from "web3";

let web3;

export default {
  data() {
    return {
      roomId: "uR8YFsKg",
      playerCount: 4,
      tokenName: "APE",
      bidIncrement: 0.1,
      minimumDeposit: 60,
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
    async startgame() {
      await this.deposit_transaction();
      this.$router.push("/game/111/waitroom");
    },
    async value() {},
    async deposit_transaction() {
      ethereum
        .request({
          method: "eth_sendTransaction",
          params: [
            {
              from: this.myAddress,
              to: "0x4520452457766B8a5C5371081b13F7B3D44C47c4",
              value: "0x29a2241af62c0000",
              gasPrice: "0x09184e72a000",
              gas: "0x2710",
            },
          ],
        })
        .then((txHash) => console.log(txHash))
        .catch((error) => console.error);

      ethereum
        .request({
          method: "eth_sendTransaction",
          params: [
            {
              from: this.myAddress,
              to: "0x2f318C334780961FB129D2a6c30D0763d9a5C970",
              value: "0x29a2241af62c0000",
              gasPrice: "0x09184e72a000",
              gas: "0x2710",
            },
          ],
        })
        .then((txHash) => console.log(txHash))
        .catch((error) => console.error);
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
