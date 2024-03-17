<template>
  <q-page>
    <div class="row q-ma-md">
        <div class="col-4">
            <q-img :src="backend+product.image" width="100%" height="380px" contain  />
        </div>
        <div class="col-8">
            <h5>{{ product.name }}</h5>
            <div>
                <div class="q-my-md">{{ product.description }}</div>
                Available Stock :{{ product.stock }} <br />
                {{ product.description }}
            </div>
            <div class="q-my-md">
              <q-btn class="" :disable="isStockZero"  @click="buyProduct(product.id)" color="primary" label="Buy Now" />
            </div>
        </div>
    </div>
    
  </q-page>
</template>
<script>
import { fetchProductDetail } from "./api/calls";
import { API_HOST } from '../../config';
export default {
  name: "DetailProduct",
  data() {
    return {
      product: {},
      backend : API_HOST,
      p_id : null
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
  created() {
    this.getProduct();
  },
  methods: {
    async getProduct() {
      // console.log(this.$route.params.id)
      this.p_id = this.$route.params.id
      // console.log(this.p_id);
      if (this.p_id) {
        await fetchProductDetail(
          this.p_id,
          {

            status: "t",
          }
        ).then((data) => {
          this.product = data.data.data;
          // console.log(this.product);
        });
      } else {
        this.$router.push({ name: "error" });
      }
    },
    buyProduct(){
      if (this.user_id != null){
        $router.push('/orderForm/'+product.id)
      }
      else{
        this.$q.notify({
            color: "red-5",
            textColor: "white",
            icon: "warning",
            message: "Please Login First"
        });
      }
    }
  },
};
</script>