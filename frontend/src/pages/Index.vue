<template>
  <div>
    <Carosel />
    <div class="q-pa-md row justify-start items-start q-gutter-md">
      <Card :product="product" v-for="product in products" :key="product.id" />
    </div>
  </div>
</template>

<script>
import Card from "components/card.vue";
import Carosel from "components/carosel.vue";
import { fetchProduct } from "./product/api/calls.js";
export default {
  name: "PageIndex",
  data() {
    return {
      products: {},
    };
  },
  components: { Carosel, Card },
  created() {
    this.getProduct();
  },
  methods: {
    async getProduct() {
      const response = await fetchProduct({
        status: "t",
        search: this.search,
      }).then((data) => {
        this.products = data.data.data;
        console.log(this.product);
      });
    },
  },
};
</script>
