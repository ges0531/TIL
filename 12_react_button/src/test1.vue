<template>
  <div id="app">
  <div class="container">
    <div class="flexContainer">
      <p><span class="blue">{{wishList[wishIdx].name}}</span> <template v-if="gap>0">까지 <span class="blue">{{animatedGap}}</span> 원 남았어요.</template>
        <template v-else>를 사고 <span class="blue">{{animatedGap*-1}}</span> 원이 남아요!</template>
      </p>
    </div>
  </div>
</div>
</template>

<script>
export default {
  el: "#app",
  data() {
    return {
      saved: Number,
      gap: 0,
      wishIdx: 0,
      wishList: [
        {
          name: "AirPods Pro",
          image:
            "https://store.storeimages.cdn-apple.com/8756/as-images.apple.com/is/MWP22?wid=2000&hei=2000&fmt=jpeg&qlt=80&op_usm=0.5,0.5&.v=1572990352299",
          price: 329000
        },
        {
          name: "iPad Pro",
          image:
            "https://store.storeimages.cdn-apple.com/8756/as-images.apple.com/is/ipad-pro-12-11-select-202003_GEO_KR?wid=445&amp;hei=550&amp;fmt=jpeg&amp;qlt=95&amp;op_usm=0.5,0.5&amp;.v=1583430766245",
          price: 1029000
        },
        {
          name: "MacBook Air",
          image:
            "https://store.storeimages.cdn-apple.com/8756/as-images.apple.com/is/macbook-air-space-gray-select-201810?wid=452&hei=420&fmt=jpeg&qlt=95&op_usm=0.5,0.5&.v=1541713862468",
          price: 1320000
        }
      ]
    };
  },
  computed: {
    animatedGap: function () {
      return this.gap.toFixed(0);
    }
  },
  watch: {
    saved: function (newValue) {
      TweenLite.to(this.$data, 0.55, {
        gap: this.wishList[this.wishIdx].price - newValue
      });
    },
    wishIdx: function (newValue) {
      TweenLite.to(this.$data, 0.55, {
        gap: this.wishList[newValue].price - this.saved
      });
    }
  },
  created() {
    this.saved = 0;
    setInterval(() => {
      this.wishIdx = (this.wishIdx + 1) % this.wishList.length;
    }, 3500);
  }

}
</script>
