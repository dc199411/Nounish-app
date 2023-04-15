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
      <img src="@/assets/images/header1.png" />
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
          <h2 class="Connect-wa">Connect your wallet to play</h2>
          <p class="wallet-disc">
            Wallets are provided by External Providers and by selecting you
            agree to Terms of those Providers.
          </p>
          <el-row :gutter="14" style="display: flex; align-items: center">
            <el-col :span="10">
              <p
                style="
                  font-size: 18px;
                  font-weight: 700;
                  line-height: 18px;
                  letter-spacing: 0.02em;
                  text-align: left;
                "
              >
                Network used this game:
              </p>
            </el-col>
            <el-col :span="10">
              <img
                class="currentchain"
                src="@/assets/images/chain/Group_ETH.png"
              />
            </el-col>
          </el-row>

          <img
            style="width: 100%"
            @click="gotoingame()"
            src="@/assets/images/wallets.png"
          />

          <!-- <el-row :gutter="10">
            <el-col :span="5">
              <div class="wallet-box" @click="connect_metamask()">
                <img src="@/assets/images/metamask.jpg" />
                <p>Metamask</p>
              </div>
            </el-col>
            <el-col :span="5">
              <div class="wallet-box" @click="movetoNextPage">
                <img src="@/assets/images/metamask.jpg" />
                <p>Metamask</p>
              </div>
            </el-col>
            <el-col :span="5">
              <div class="wallet-box">
                <img src="@/assets/images/metamask.jpg" />
                <p>Metamask</p>
              </div>
            </el-col>
            <el-col :span="5">
              <div class="wallet-box">
                <img src="@/assets/images/metamask.jpg" />
                <p>Metamask</p>
              </div>
            </el-col>
            <el-col :span="5">
              <div class="wallet-box">
                <img src="@/assets/images/metamask.jpg" />
                <p>Metamask</p>
              </div>
            </el-col>
            <el-col :span="5">
              <div class="wallet-box">
                <img src="@/assets/images/metamask.jpg" />
                <p>Metamask</p>
              </div>
            </el-col>
            <el-col :span="5">
              <div class="wallet-box">
                <img src="@/assets/images/metamask.jpg" />
                <p>Metamask</p>
              </div>
            </el-col>
          </el-row> -->
        </el-col>
      </el-row>
    </el-main>

    <el-footer class="footer">
      <img src="@/assets/images/footer.png" />
    </el-footer>
  </el-container>
</template>

<script>
// const Cookie = process.client ? require("js-cookie") : undefined;
import MetaMaskSDK from "@metamask/sdk";
import Web3 from "web3";

export default {
  data() {
    return {
      roomId: this.$route.params.id,
      metamaskoptions: {
        injectProvider: false,
        communicationLayerPreference: "webrtc",
      },
      ethereum: {},
      shishiodoshirisk: [],
    };
  },
  created() {},
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

    await this.switchEthereumChain();
  },
  methods: {
    gotoingame() {
      this.connect_metamask();
      this.$router.push("/game/" + this.roomId + "/depositroom");
    },
    async value() {},
    connect_metamask() {
      console.log("pushed ");
      ethereum
        .request({ method: "eth_requestAccounts" })
        // .then(handleAccountsChanged)
        .catch((error) => {
          if (error.code === 4001) {
            // EIP-1193 userRejectedRequest error
            console.log("Please connect to MetaMask.");
          } else {
            console.error(error);
          }
        });
    },
    async switchEthereumChain() {
      try {
        await ethereum.request({
          method: "wallet_switchEthereumChain",
          params: [{ chainId: "0xf00" }],
        });
      } catch (switchError) {
        // This error code indicates that the chain has not been added to MetaMask.
        if (switchError.code === 4902) {
          try {
            await ethereum.request({
              method: "wallet_addEthereumChain",
              params: [
                {
                  chainId: "0xAEF3",
                  chainName: "Celo Alfajores",
                  nativeCurrency: {
                    name: "CELO",
                    symbol: "CELO", // 2-6 characters long
                    decimals: 18,
                  },
                  rpcUrls: ["https://alfajores-forno.celo-testnet.org"],
                  blockExplorerUrls: ["https://alfajores.celoscan.io"],
                },
              ],
            });
          } catch (addError) {
            // handle "add" error
          }
        }
        // handle other "switch" errors
      }
    },
  },
};
</script>

<style>
.currentchain {
  height: 36px;
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

.doc-link {
  font-size: 18px;
  font-weight: bold;
}

.header-contents {
  display: flex;
  align-items: center;
}
</style>
