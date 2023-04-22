<template>
  <img @click="gotogame()" src="@/assets/images/toppage.png" />
</template>

<script>
export default {
  data() {
    return {};
  },

  async mounted() {},

  methods: {
    async value() {},
    gotogame() {
      this.$router.push("/game/11");
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
img {
  width: 100%;
}
</style>
