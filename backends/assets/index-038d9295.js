import{c8 as C,c2 as S,c9 as k,ca as _,c6 as I}from"./index-27b2444c.js";import{bs as B,r as n,a3 as c,j as R,k as F,D as e,x as t,l as r,B as N,C as q,b6 as D,b4 as E}from"./_plugin-vue_export-helper-a4851b7b.js";const P=u=>(D("data-v-ff82c5a3"),u=u(),E(),u),T={class:"login-container"},U={class:"title-container"},$=P(()=>r("h3",{class:"title"},"flask-vue-cms",-1)),j={class:"svg-container svg-container_login"},L={class:"svg-container"},z={__name:"index",setup(u){const s=n({username:"admin",password:"admin"}),f=C();function v(i,o,l){o.length<3?l(new Error(f.t("msg.login.passwordRule"))):l()}const w=n({username:[{required:!0,trigger:"blur",message:f.t("msg.login.usernameRule")}],password:[{required:!0,trigger:"blur",validator:v}]}),a=n("password");function h(){a.value==="password"?a.value="":a.value="password"}const d=n(!1),g=n(null),y=S();function x(){g.value.validate(i=>{i&&(d.value=!0,y.login(s.value).then(()=>{d.value=!1,I.push("/")}).catch(o=>{console.log(o),d.value=!1}))})}return(i,o)=>{const l=c("el-input"),p=c("el-form-item"),b=c("el-button"),V=c("el-form");return R(),F("div",T,[e(V,{autoComplete:"on",model:s.value,rules:w.value,ref_key:"loginFormRef",ref:g,"label-position":"left","label-width":"0px",class:"card-box login-form"},{default:t(()=>[r("div",U,[$,e(k,{class:"lang-select"})]),e(p,{prop:"username"},{default:t(()=>[r("span",j,[e(_,{icon:"user"})]),e(l,{name:"username",type:"text",modelValue:s.value.username,"onUpdate:modelValue":o[0]||(o[0]=m=>s.value.username=m),autoComplete:"on",placeholder:"username"},null,8,["modelValue"])]),_:1}),e(p,{prop:"password"},{default:t(()=>[r("span",L,[e(_,{icon:"password"})]),e(l,{name:"password",type:a.value,modelValue:s.value.password,"onUpdate:modelValue":o[1]||(o[1]=m=>s.value.password=m),autoComplete:"on",placeholder:"password"},null,8,["type","modelValue"]),r("span",{class:"show-pwd",onClick:h},[e(_,{icon:a.value==="password"?"eye":"eye-open"},null,8,["icon"])])]),_:1}),e(p,null,{default:t(()=>[e(b,{type:"primary",style:{width:"100%"},onClick:x},{default:t(()=>[N(q(i.$t("msg.login.loginBtn")),1)]),_:1})]),_:1})]),_:1},8,["model","rules"])])}}},H=B(z,[["__scopeId","data-v-ff82c5a3"]]);export{H as default};
