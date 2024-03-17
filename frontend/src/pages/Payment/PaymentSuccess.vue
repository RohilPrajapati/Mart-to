<template>
  <div class="text-center">
    <div class="bg-green-5 q-py-md">
      <span class="text-h4">Playment is successFull</span>
    </div>
    <q-btn
      @click="$router.push({name:'my_order'})"
      class="q-mt-md"
      color="green-5"
      text-color="white"
      label="My Order"
    />
  </div>
</template>

<script>
import { addPaymentData } from  "./api/calls"
export default {
  data() {
    return {
      formData: {
        refId: this.$route.query.refId,
        oid: this.$route.query.oid,
        amt: this.$route.query.amt,
      },
    };
  },
  created() {
    this.postPaymentData()
  },
  methods: {
    async postPaymentData() {
      await addPaymentData(this.formData)
        .then((data) => {
        console.log("request send")
          this.$q.notify({
            color: "green-5",
            textColor: "white",
            icon: "info",
            message: data.data.message,
          });
        //   this.$router.push({name:'my_order'})
        })
        .catch((error) => {
            console.log(error)
          this.$q.notify({
            color: "red-5",
            textColor: "white",
            icon: "warning",
            
            message: error.response.data.message,
          });
        });
    },
  },
};
</script>
<style>
</style>