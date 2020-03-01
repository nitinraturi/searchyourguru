<template>
  <div id="home_view" class="has-background-white">
    <section class="hero is-info is-bold is-medium">
      <div class="hero-body">
        <div class="container-fluid">
          <div class="columns is-centered">
            <div class="column is-8">
              <p class="title is-5">
                Search for a tuition - Enter locality or pincode and subject
              </p>
              <div class="box">
                <FilterForm />
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <h1 class="title is-4 has-text-centered">About Us</h1>
        <div class="columns is-centered">
          <div class="column is-8">
            <h2 class="title is-6">
              What is <span class="has-text-info">searchyourguru.com</span>
            </h2>
            <p class="subtitle is-size-6">
              SearchYourGuru is India's tuitions platform. We have more than
              1000+ categories or subjects to choose from.
            </p>
            <br />
            <h2 class="title is-6">
              Our <span class="has-text-info">Vision</span>
            </h2>
            <p class="subtitle is-size-6">
              Our vision is to be one-stop learning partner for every Indian.
            </p>
          </div>
        </div>
      </div>
      <hr />
    </section>

    <section class="section has-background-light-er">
      <div class="container">
        <h1 class="title is-4 has-text-centered">How SearchYourGuru Works</h1>
        <div class="columns is-multiline is-mobile">
          <div class="column is-4 has-text-centered">
            <p class="subtitle">
              <span class="tag is-info is-rounded is-large">1</span>
            </p>
            <center>
              <figure class="image is-128x128">
                <img src="@/assets/requirements.svg" alt="" />
              </figure>
              <hr />
            </center>
            <h1 class="title is-6">Search for your requirements</h1>
            <p class="subtitle is-6">
              Want to learn something? Just enter details such as subject or
              category, locality and preference.
            </p>
          </div>
          <div class="column is-4 has-text-centered">
            <p class="subtitle">
              <span class="tag is-info is-rounded is-large">2</span>
            </p>
            <center>
              <figure class="image is-128x128">
                <img src="@/assets/customised_tutions.svg" alt="" />
              </figure>
              <hr />
            </center>
            <h1 class="title is-6">Get customised tuitions</h1>
            <p class="subtitle is-6">
              Based on your requirement you will be shown customised tuitions
              from tutors.
            </p>
          </div>
          <div class="column is-4 has-text-centered">
            <p class="subtitle">
              <span class="tag is-info is-rounded is-large">3</span>
            </p>
            <center>
              <figure class="image is-128x128">
                <img src="@/assets/classroom.svg" alt="" />
              </figure>
              <hr />
            </center>
            <h1 class="title is-6">Compare & request a demo</h1>
            <p class="subtitle is-6">
              Once you get tuitions, you can compare them and choose the ones
              that fit your learning requirement and request a demo.
            </p>
          </div>
        </div>
        <center v-if="isAuthenticated == false">
          <router-link to="/signup/" class="button is-info is-outlined">
            Register & Start Learning
          </router-link>
        </center>
      </div>
      <hr />
    </section>
    <section class="section">
      <div class="container">
        <h1 class="title is-4 has-text-centered">Teach & Earn</h1>
        <div class="columns is-centered">
          <div class="column is-9">
            <div class="columns is-multiline is-mobile">
              <div class="column is-6">
                <div class="columns is-mobile">
                  <div class="column is-2">
                    <p class="subtitle">
                      <span class="tag is-link is-rounded">1</span>
                    </p>
                  </div>
                  <div class="column is-10">
                    <h1 class="title is-6">Create an account</h1>
                    <p class="subtitle is-6">
                      To teach,
                      <span class="has-text-info has-text-bolder"
                        >register as a tutor</span
                      >
                      using your email address and verify using the verification
                      link.
                    </p>
                  </div>
                </div>
              </div>
              <div class="column is-6">
                <div class="columns is-mobile">
                  <div class="column is-2">
                    <p class="subtitle">
                      <span class="tag is-link is-rounded">2</span>
                    </p>
                  </div>
                  <div class="column is-10">
                    <h1 class="title is-6">Post a new tution</h1>
                    <p class="subtitle is-6">
                      In Dashboard, Click on
                      <span class="has-text-info">Create Tution +</span> button
                      and fill your tution details such as title, description,
                      price, etc.
                    </p>
                  </div>
                </div>
              </div>
              <div class="column is-6">
                <div class="columns is-mobile">
                  <div class="column is-2">
                    <p class="subtitle">
                      <span class="tag is-link is-rounded">3</span>
                    </p>
                  </div>
                  <div class="column is-10">
                    <h1 class="title is-6">Tution Request</h1>
                    <p class="subtitle is-6">
                      In Tution section in dashboard there is a field named
                      <span class="has-text-info">Applications</span>, check
                      your applicants details there.
                    </p>
                  </div>
                </div>
              </div>
              <div class="column is-6">
                <div class="columns is-mobile">
                  <div class="column is-2">
                    <p class="subtitle">
                      <span class="tag is-link is-rounded">4</span>
                    </p>
                  </div>
                  <div class="column is-10">
                    <h1 class="title is-6">Get Hired</h1>
                    <p class="subtitle is-6">
                      Once got applicants, you can
                      <span class="has-text-info">contact</span> them through
                      the information provided in your dashboard.
                    </p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <center v-if="isAuthenticated == false">
          <router-link to="/signup/" class="button is-info is-outlined">
            Register & Start Earning
          </router-link>
        </center>
      </div>
    </section>
    <section class="section">
      <div class="container">
        <h1 class="title is-4 has-text-centered">
          Contact Us - How can we help?
        </h1>
        <div class="columns is-centered">
          <div class="column is-8">
            <div class="box">
              <ContactForm />
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import FilterForm from '@/components/forms/FilterForm.vue'
import ContactForm from '@/components/forms/ContactForm.vue'
export default {
  name: 'home',
  components: {
    FilterForm,
    ContactForm
  },
  computed: {
    isAuthenticated() {
      return this.$store.state.isAuthenticated
    }
  }
}
</script>
