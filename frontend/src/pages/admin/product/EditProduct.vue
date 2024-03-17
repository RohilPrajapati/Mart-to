<template>
  <q-page>
    <div class="q-ma-sm text-center">
      <h5>Update Product</h5>
      <q-form class="form">
        <q-input class="q-my-md" rounded outlined v-model="product.name" label="Name" />
        <q-input
          v-model="product.description"
          rounded
          label="Description"
          outlined
          type="textarea"
          class="q-my-md"
          :input-style="{resize: 'none'}"
        />
        <q-input
          class="q-my-md"
          rounded
          outlined
          v-model="product.stock"
          type="number"
          label="Stock"
        />
        <q-input
          class="q-my-md"
          rounded
          outlined
          v-model="product.price"
          type="number"
          label="Price"
        />
        <q-file
          @input="val => { file = val[0] }"
          rounded
          outlined
          class="q-my-md"
          label="Upload Image"
          v-model="image"
        >
          <template v-slot:prepend>
            <q-icon name="image" />
          </template>
        </q-file>
        <q-toggle class="q-my-md" v-model="product.status" label="Status" />
        <br />
        <q-btn class="q-mr-sm" @click="editProduct()" color="blue" label="Update" />
        <q-btn color="red-7" @click="$router.push({name: 'adminproduct'})" label="Cancel" />
      </q-form>
    </div>
  </q-page>
</template>
<script>
import { updateProduct, getProduct } from "./api/calls";
export default {
  name: "AdminProductAdd",
  data() {
    return {
      product_id: this.$route.query.id,
      product: {},
      image: null,
    };
  },
  created() {
    this.fetchProduct();
  },
  methods: {
    async editProduct() {
      const formData = new FormData();
      // this.product.image = null
      Object.keys(this.product).forEach((key) => {
        if (key != "image") {
          formData.append(key, this.product[key]);
        } else {
          if (this.image != null) {
            formData.append(key, this.image);
          }
        }
      });
      if (this.product.name == "") {
        this.$q.notify({
          color: "red-5",
          textColor: "white",
          icon: "warning",
          message: "Name of Product Is required",
        });
      } else if (this.product.description == "") {
        this.$q.notify({
          color: "red-5",
          textColor: "white",
          icon: "warning",
          message: "description is required",
        });
      } else if (this.product.stock == "") {
        this.$q.notify({
          color: "red-5",
          textColor: "white",
          icon: "warning",
          message: "Stock is required",
        });
      } else if (this.product.price == "") {
        this.$q.notify({
          color: "red-5",
          textColor: "white",
          icon: "warning",
          message: "Price is required",
        });
      } else {
        await updateProduct(this.product_id, formData)
          .then((data) => {
            this.$q.notify({
              color: "green-5",
              textColor: "white",
              icon: "info",
              message: "Product have been Update",
            });
            this.$router.push({ name: "adminproduct" });
          })
          .catch((error) => {
            this.$q.notify({
              color: "red-5",
              textColor: "white",
              icon: "warning",
              message: "Fail to Update Product",
            });
          });
      }
    },
    async fetchProduct() {
      await getProduct(this.product_id).then((response) => {
        this.product = response.data.data;
      });
    },
  },
};
</script>
<style scoped>
.form {
  width: 50%;
  margin: 10px auto;
}
</style>