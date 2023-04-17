<template>
  <PowerliftingForm @analyzeLiftsData="onFormSubmit" v-show="shouldDisplayForm"/>
  <PowerliftingResults :liftData="liftData" v-if="shouldLoadResults"/>
</template>

<script>
import PowerliftingForm from './PowerliftingForm.vue';
import PowerliftingResults from './PowerliftingResults.vue';

export default {
  name: 'PowerliftingHomePage',
  components: {
    PowerliftingForm,
    PowerliftingResults,
  },
  data() {
    return {
      shouldLoadResults: false,
      shouldDisplayForm: true,
      liftData: {},
    };
  },
  methods: {
    onFormSubmit(data) {
      // This is where you will update everything with emitted data
      this.liftData = data;
      this.shouldLoadResults = true;
    },
  },
};
</script>
