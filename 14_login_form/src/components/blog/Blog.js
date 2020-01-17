import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import CssBaseline from '@material-ui/core/CssBaseline';
import Grid from '@material-ui/core/Grid';
import Container from '@material-ui/core/Container';
import GitHubIcon from '@material-ui/icons/GitHub';
import FacebookIcon from '@material-ui/icons/Facebook';
import TwitterIcon from '@material-ui/icons/Twitter';
import Header from './Header';
import MainFeaturedPost from './MainFeaturedPost';
import FeaturedPost from './FeaturedPost';
import Main from './Main';
import Sidebar from './Sidebar';
import Footer from './Footer';
import post1 from './blog-post.1.md';
import post2 from './blog-post.2.md';
import post3 from './blog-post.3.md';

const useStyles = makeStyles(theme => ({
  mainGrid: {
    marginTop: theme.spacing(3),
  },
}));

const sections = [
  { title: 'Technology', url: '#' },
  { title: 'Design', url: '#' },
  { title: 'Culture', url: '#' },
  { title: 'Business', url: '#' },
  { title: 'Politics', url: '#' },
  { title: 'Opinion', url: '#' },
  { title: 'Science', url: '#' },
  { title: 'Health', url: '#' },
  { title: 'Style', url: '#' },
  { title: 'Travel', url: '#' },
];

const mainFeaturedPost = {
  title: '쉽고 간편한 정치 사이트',
  description:
    "손쉽게 후보들의 공약과 정책을 살펴보세요!",
  image: 'http://www.assembly.go.kr/common/imagefile.do?fid=bbs&bbs_cd_n=46&bbs_seq_n=2&file_seq_n=1',
  imgText: 'main image description',
  linkText: '싸피는하나당 활용 가이드',
};

const featuredPosts = [
  {
    title: '대한민국 제19대 대통령 문재인',
    date: '2017.05.10 - 2022.05.10',
    description:
      '사람이 먼저다. - 18대 대선 당시 문재인의 캐치프레이즈',
    image: 'http://kr.people.com.cn/NMediaFile/2017/1213/FOREIGN201712131333000564275515411.jpg',
    imageText: 'Image Text',
  },
  {
    title: '제21대 국회의원 선거',
    date: '2020.04.15',
    description:
      '이번 선거는 문재인 정부의 평가를 가르는 중간선거이기도 하다. 따라서 선거 결과가 문재인 정부의 국정 운영에 중대한 영향을 미칠 것이며, 2년 뒤 대선에서 과연 어느 정당의 후보가 국민의 선택을 받느냐도 이 선거의 결과에 따라 윤곽이 잡힐 것으로 보인다.',
    image: 'https://dimg.donga.com/i/600/0/90/ugc/CDB/WEEKLY/Article/5d/71/c1/ef/5d71c1ef1c5cd2738de6.jpg',
    imageText: 'Image Text',
  },
];

const posts = [post1, post2, post3];

const sidebar = {
  title: 'About',
  description:
    'Etiam porta sem malesuada magna mollis euismod. Cras mattis consectetur purus sit amet fermentum. Aenean lacinia bibendum nulla sed consectetur.',
  archives: [
    { title: 'March 2020', url: '#' },
    { title: 'February 2020', url: '#' },
    { title: 'January 2020', url: '#' },
    { title: 'November 1999', url: '#' },
    { title: 'October 1999', url: '#' },
    { title: 'September 1999', url: '#' },
    { title: 'August 1999', url: '#' },
    { title: 'July 1999', url: '#' },
    { title: 'June 1999', url: '#' },
    { title: 'May 1999', url: '#' },
    { title: 'April 1999', url: '#' },
  ],
  social: [
    { name: 'GitHub', icon: GitHubIcon },
    { name: 'Twitter', icon: TwitterIcon },
    { name: 'Facebook', icon: FacebookIcon },
  ],
};

export default function Blog() {
  const classes = useStyles();

  return (
    <React.Fragment>
      <CssBaseline />
      <Container maxWidth="lg">
      <Header title="싸피는 하나당" sections={sections} />
        <main>
          <MainFeaturedPost post={mainFeaturedPost} />
          <Grid container spacing={4}>
            {featuredPosts.map(post => (
              <FeaturedPost key={post.title} post={post} />
            ))}
          </Grid>
          <Grid container spacing={5} className={classes.mainGrid}>
            <Main title="From the firehose" posts={posts} />
            <Sidebar
              title={sidebar.title}
              description={sidebar.description}
              archives={sidebar.archives}
              social={sidebar.social}
            />
          </Grid>
        </main>
      </Container>
      <Footer title="Footer" description="Something here to give the footer a purpose!" />
    </React.Fragment>
  );
}