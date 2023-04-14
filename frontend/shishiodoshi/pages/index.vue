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
      <el-row :gutter="84">
        <el-col :span="10">
          <img src="images/game/game-4p-start.png" />
        </el-col>
        <el-col :span="10">
          <h2 class="Connect-wa">Connect your wallet to play</h2>
          <p class="wallet-disc">
            Wallets are provided by External Providers and by selecting you
            agree to Terms of those Providers.
          </p>
          <el-row :gutter="10">
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
          <el-row :gutter="10">
            <el-col :span="10">
              <div class="wallet-box">
                <img src="images/game/game-4p-start.png" />
              </div>
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
        </el-col>
      </el-row>
      <div>
        <div class="links">
          <a
            href="https://nuxtjs.org/"
            target="_blank"
            rel="noopener noreferrer"
            class="button--green"
          >
            Documentation
          </a>
          <a
            href="https://github.com/nuxt/nuxt.js"
            target="_blank"
            rel="noopener noreferrer"
            class="button--grey"
          >
            GitHub
          </a>
        </div>
      </div>
    </el-main>

    <el-footer> </el-footer>
  </el-container>
  <!-- <div class="container">
    
  </div> -->
</template>

<script lang="ts" setup>
import { ref } from "vue";

const value = ref("");

const options = [
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
];
</script>

<style>
.container {
  margin: 42px 84px;
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
</style>
