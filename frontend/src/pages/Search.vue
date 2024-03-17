<template>
    <div>
        <div class="q-pa-md row justify-start items-start q-gutter-md">
      <Card :product="product" v-for="product in products" :key="product.id" />
    </div>
    </div>
</template>
<script>
import Card  from "components/card.vue";
import { fetchProduct } from "./product/api/calls.js";
export default {
  name: "search",
  data() {
    return {
      products: {},
    };
  },
  components: {  Card },
  watch:{
    '$route.query.search'(newSearch,oldSearch) {
        this.getProduct()
    }
  },
  created() {
    this.getProduct();
  },
  computed:{
    search(){
        return this.$route.query.search
    }
  },
  methods: {
    async getProduct() {
      await fetchProduct({
        status: "t",
        search: this.search,
      }).then((data) => {
        this.products = data.data.data;
      });
    },
  },
};
</script>