<template>
  <q-page>
    <div class="q-ma-sm text-center">
      <h5>Add Product</h5>
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
          v-model="product.image"
        >
          <template v-slot:prepend>
            <q-icon name="image" />
          </template>
        </q-file>
        <q-toggle class="q-my-md" v-model="product.status" label="Status" />
        <br />
        <q-btn class="q-mr-sm" @click="addProduct()" color="blue" label="Add" />
        <q-btn color="red-7" @click="$router.push({name: 'adminproduct'})" label="Cancel" />
      </q-form>
    </div>
  </q-page>
</template>
<script>
import { createProduct } from "./api/calls";
export default {
  name: "AdminProductAdd",
  data() {
    return {
      product: {
        name: "",
        description: "",
        stock: null,
        price: null,
        image: "",
        status: true,
      },
    };
  },
  methods: {
    async addProduct() {
      const formData = new FormData();
      Object.keys(this.product).forEach((key) => {
        formData.append(key, this.product[key]);
      });
      if (this.product.name == "") {
        this.$q.notify({
              color: "red-5",
              textColor: "white",
              icon: "warning",
              message: "Name of Product Is required",
            });
      } 
      else if (this.product.description == "") {
        this.$q.notify({
              color: "red-5",
              textColor: "white",
              icon: "warning",
              message: "description is required",
            });
      }
      else if (this.product.stock == "") {
        this.$q.notify({
              color: "red-5",
              textColor: "white",
              icon: "warning",
              message: "Stock is required",
            });
      }
      else if (this.product.price == "") {
        this.$q.notify({
              color: "red-5",
              textColor: "white",
              icon: "warning",
              message: "Price is required",
            });
      }
      else if (this.product.image == "") {
        this.$q.notify({
              color: "red-5",
              textColor: "white",
              icon: "warning",
              message: "Image is required",
            });
      }
      else {
        await createProduct(formData)
          .then((data) => {
            this.$q.notify({
              color: "green-5",
              textColor: "white",
              icon: "info",
              message: "Product have been added",
            });
          })
          .catch((error) => {
            this.$q.notify({
              color: "red-5",
              textColor: "white",
              icon: "warning",
              message: "Fail to add Product",
            });
          });
      }
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