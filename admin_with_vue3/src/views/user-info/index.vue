<template>
  <div class="user-info-container">
    <el-card shadow="hover" class="head-container">
      <el-button class="header-btn" type="primary" v-print="printObj"
        >{{ $t('msg.userInfo.print') }}
      </el-button>
    </el-card>
    <el-card shadow="never" class="body-container" id="userInfoBox">
      <template #header>
        <h2 class="title">{{ $t('msg.userInfo.title') }}</h2>
      </template>
      <template #default>
        <div class="section-one">
          <el-descriptions :column="2" border>
            <el-descriptions-item :label="$t('msg.userInfo.name')"
              >{{ userInfo.username }}
            </el-descriptions-item>
            <el-descriptions-item :label="$t('msg.userInfo.sex')"
              >{{ userInfo.gender }}
            </el-descriptions-item>
            <el-descriptions-item :label="$t('msg.userInfo.nation')"
              >{{ userInfo.nationality }}
            </el-descriptions-item>
            <el-descriptions-item :label="$t('msg.userInfo.mobile')"
              >{{ userInfo.mobile }}
            </el-descriptions-item>
            <el-descriptions-item :label="$t('msg.userInfo.province')"
              >{{ userInfo.province }}
            </el-descriptions-item>
            <el-descriptions-item :label="$t('msg.userInfo.date')"
              >{{ userInfo.openTime }}
            </el-descriptions-item>
            <el-descriptions-item :label="$t('msg.userInfo.remark')" :span="2">
              <el-tag
                class="remark"
                v-for="(item, index) in userInfo.remark"
                :key="index"
                size="small"
              >
                {{ item }}
              </el-tag>
            </el-descriptions-item>
            <el-descriptions-item :label="$t('msg.userInfo.address')" :span="2"
              >{{ userInfo.address }}
            </el-descriptions-item>
          </el-descriptions>
          <el-avatar
            class="avatar"
            :src="userInfo.avatar"
            :size="200"
            shape="square"
          ></el-avatar>
        </div>
        <div class="section-two">
          <el-descriptions direction="vertical" :column="1" border>
            <el-descriptions-item :label="$t('msg.userInfo.experience')">
              <ul>
                <li v-for="(item, index) in userInfo.experience" :key="index">
                  <span>{{ item.startTime }} ---- {{ item.endTime }}</span>
                  <span>{{ item.title }}</span>
                  <span>{{ item.desc }}</span>
                </li>
              </ul>
            </el-descriptions-item>
            <el-descriptions-item :label="$t('msg.userInfo.major')"
              >{{ userInfo.major }}
            </el-descriptions-item>
            <el-descriptions-item :label="$t('msg.userInfo.glory')"
              >{{ userInfo.glory }}
            </el-descriptions-item>
          </el-descriptions>
        </div>
        <div class="footer">
          {{ $t('msg.userInfo.foot') }}
        </div>
      </template>
    </el-card>
  </div>
</template>

<script setup>
// 为了该页面既能以页面的形式，又能以弹窗的形式，采用props传入
import { userDetail } from '@/api/user'
import { ref } from 'vue'

const props = defineProps({
  id: {
    type: String,
    required: true
  }
})

const userInfo = ref({})

async function getUserInfo() {
  userInfo.value = await (await userDetail(props.id)).data
  console.log(userInfo.value, 22)
}

getUserInfo()

const printObj = {
  id: 'userInfoBox',
  popTitle: 'the user info'
}
</script>

<style lang="scss" scoped>
:deep(.head-container) .el-card__body {
  display: flex;

  .header-btn {
    margin-left: auto;
  }
}

.body-container {
  margin-top: 20px;

  .title {
    text-align: center;
  }

  .section-one {
    display: flex;
    .el-descriptions {
      flex-grow: 1;
    }
    .avatar {
      background: transparent;
      padding: 30px 20px;
      border: 1px solid #ebeef5;
      border-left: none;
    }
  }

  .section-two {
    li {
      list-style: none;
    }
    span {
      margin-right: 10px;
    }
  }

  .footer {
    text-align: right;
    margin-top: 20px;
  }
}
</style>
