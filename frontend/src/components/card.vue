<template>
  <q-card  class="my-card">
    <div @click="$router.push('/product/'+product.id)" style="cursor:pointer">
      <q-img :src="backend+product.image" contain style="height: 250px; width: 100%" />

      <q-card-section>
        <div class="row no-wrap items-center">
          <div class="col text-h6 ellipsis">{{product.name}}</div>
        </div>
      </q-card-section>

      <q-card-section class="q-pt-none">
        <div class="text-subtitle1">Rs・{{product.price}}</div>
        <!-- <div class="text-caption text-grey">
              {{description}}
        </div>-->
      </q-card-section>
      <q-separator />
    </div>

    <q-card-actions class="justify-between">
      <span>Available Stock {{product.stock}}</span>
      <span>
        <q-btn flat round @click="noAvailable()" icon="shopping_cart" />
        <q-btn
          :disable="isStockZero"
          flat
          style="background-color:#26abdd; color:white"
          @click="checkLoginStatus()"
        >buy</q-btn>
      </span>
      <!-- <q-btn flat style="background-color:#26abdd; color:white" @click="$router.push('/product/'+product.id)">Detail</q-btn> -->
    </q-card-actions>
  </q-card>
</template>

<script>
import { API_HOST } from "../config/index.js";
import { Store } from "../store/index";
export default {
  name: "Card",
  data() {
    return {
      backend: API_HOST,
      user_id: Store.state.user.user.user_id,
    };
  },
  computed: {
    isStockZero() {
      if (this.product.stock == 0) {
        return true;
      }
      return false;
    },
  },
  props: { product: { required: true } },
  methods: {
    noAvailable() {
      this.$q.notify({
        color: "red-5",
        textColor: "white",
        icon: "info",
        message: "Currently this feature is Not available",
      });
    },
    checkLoginStatus() {
      if (this.user_id != null) {
        this.$router.push("/orderForm/" + this.product.id);
      } else {
        this.$q.notify({
          color: "red-5",
          textColor: "white",
          icon: "warning",
          message: "Please Login First",
        });
      }
    },
  },
};
</script>

<style lang="sass" scoped>
.my-card
  width: 100%
  max-width: 300px
</style>