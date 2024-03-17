
const routes = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/Index.vue'), name: "home" },
      { path: 'search/', component: () => import('pages/Search.vue'), name: "search" },
      { path: 'login/', component: () => import('pages/user/Login.vue'), name: "login" },
      { path: 'signup/', component: () => import('pages/user/Signup.vue'), name: "register" },
      { path: 'profile/', component: () => import('pages/user/Profile.vue'), name: "profile" },
      { path: 'product/:id', component: () => import('pages/product/ProductDetail.vue'), name: "detailProduct" },
      { path: 'cart/', component: () => import('pages/Cart/Cart.vue'), name: "Cart" },
      { path: 'orderForm/:id', component: () => import('pages/Order/OrderForm.vue'), name: "orderForm" },
      { path: 'payment/', component: () => import('pages/Order/Payment.vue'), name: "payment" },
      { path: 'payment/success/', component: () => import('pages/Payment/PaymentSuccess.vue'), name: "payment_success" },
      { path: 'payment/fail/', component: () => import('pages/Payment/PaymentFail.vue'), name: "payment_fail" },
      { path: 'myOrder/', component: () => import('pages/Order/OrderList.vue'), name: "my_order" },
      { path: 'myOrder/detail/', component: () => import('pages/Order/OrderDetail.vue'), name: "order_detail" },
    ]
  },
  {
    path: '/admin',
    component: () => import('layouts/AdminMainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/admin/Admin.vue'), name: "admin" },
      { path: 'dashboard/', component: () => import('pages/admin/Dashboard.vue'), name: "admindashboard" },
      { path: 'user/', component: () => import('pages/admin/User/UserList.vue'), name: "adminUserList" },
      { path: 'product/', component: () => import('pages/admin/product/Product.vue'), name: "adminproduct" },
      { path: 'product/add/', component: () => import('pages/admin/product/AddProduct.vue'), name: "adminproductadd" },
      { path: 'product/edit/', component: () => import('pages/admin/product/EditProduct.vue'), name: "adminproductedit" },
      { path: 'order/', component: () => import('pages/admin/Order/OrderList.vue'), name: "admin_order_list" },
      { path: 'order/detail/', component: () => import('pages/admin/Order/AdminOrderDetail.vue'), name: "admin_order_detail" },
    ]
  },
  {
    path: '/admin/login',
    component: () => import('pages/admin/User/Login.vue'),
    name: "admin_login",
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '*',
    component: () => import('pages/Error404.vue'),
    name: 'error'
  }
]

export default routes
