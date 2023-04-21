<template>
  <b-container fluid class="powerliftingPageContainer">

    <b-row align-v="center" class="powerliftingPageRow" v-if="displayResults">

      <b-col cols=12>
        <PowerliftingResults :liftData="liftData"/>

        <div v-if="displaySpinner">
          <b-spinner label="Spinning"></b-spinner>
        </div>
      </b-col>

    </b-row>

    <b-row align-v="center" class="powerliftingPageRow" v-else>

      <b-col cols=12>
        <PowerliftingForm
          @requestSubmitted="onFormSubmit"
          @analyzeLiftsData="onFormReturn"
          v-show="displayForm"
        />
      </b-col>

    </b-row>

  </b-container>
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
      displayResults: false,
      displayForm: true,
      displaySpinner: false,
      liftData: {},
    };
  },
  methods: {
    onFormSubmit() {
      this.displaySpinner = true;
    },
    onFormReturn(data) {
      // This is where you will update everything with emitted data
      this.liftData = data;
      this.displaySpinner = false;
      this.displayResults = true;
    },
  },
};
</script>
