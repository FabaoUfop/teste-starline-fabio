<template>
  <div id="exemplo">
    <table class="table">
      <thead>
        <th><a href="#" @click="sort($event, 'fields.usuario')">Usuario</a></th>
        <th><a href="#" @click="sort($event, 'fields.questao_pergunta')">Questao</a></th>
        <th><a href="#" @click="sort($event, 'fields.questao_tipo')">Tipo</a></th>
      </thead>
      <tbody>
        <tr v-for="questao in lista">
          <td>{{ questao.fields.usuario }}</td>
          <td>{{ questao.fields.questao_pergunta }}</td>
            <td>{{ questao.fields.questao_tipo }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>
<script>
export default {
  data() {
    return {
      sortDirection: 'desc',
      lista: []
    }
  },
  mounted() {
    this.$http.get("/app/questoes").then( (req) => this.lista = req.data )
  },
  methods:{
    sort(event, campo){
      event.preventDefault()
      if ( this.sortDirection == "desc" )
      {
          this.sortDirection = "asc"
      }else{
        this.sortDirection = "desc"
      }
      this.lista = _.orderBy(this.lista, campo, this.sortDirection)
    }
  }
}
</script>
<style>
  #exemplo{
      color: red;
  }
</style>
