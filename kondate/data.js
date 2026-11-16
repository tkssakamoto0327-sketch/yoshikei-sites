/* =========================================================
   ヨシケイキッチン 献立表データ
   ・毎週の更新はこのファイルだけを編集します（index.html は触らない）
   ・weeks に1週分を追加：start はその週の月曜（YYYY-MM-DD）
   ・値は Googleドライブ PDF のファイルID（URLの /d/ と /view の間）
     または サイト内PDF 'pdf/YYYY-MM-DD_コース.pdf'
   ・まだ無いコースは書かない／空文字にすると「準備中」と表示
   ・過去の週は自動で非表示になるので、消さなくても大丈夫です
   ========================================================= */
window.KONDATE = {
  recipeUrl: 'https://yoshikei-recipe.pages.dev/',
  courses: [
    { key: 'tezukuri',      name: '手づくりおかず',         color: '#CCFFCC' },
    { key: 'kantan',        name: '簡単おかず',             color: '#FFC000' },
    { key: 'chokantan',     name: '超簡単おかず',           color: '#FF9966' },
    { key: 'volume',        name: 'ボリューム手作りおかず', color: '#FF99CC' },
    { key: 'chokantanplus', name: '超簡単プラス',           color: '#B8CCE4' }
  ],
  weeks: [
    { start: '2026-11-16', files: {
      tezukuri: 'pdf/2026-11-16_tezukuri.pdf',
      kantan: 'pdf/2026-11-16_kantan.pdf',
      chokantan: 'pdf/2026-11-16_chokantan.pdf',
      volume: 'pdf/2026-11-16_volume.pdf',
      chokantanplus: 'pdf/2026-11-16_chokantanplus.pdf' } },
    { start: '2026-11-23', files: {
      tezukuri: 'pdf/2026-11-23_tezukuri.pdf',
      kantan: 'pdf/2026-11-23_kantan.pdf',
      chokantan: 'pdf/2026-11-23_chokantan.pdf',
      volume: 'pdf/2026-11-23_volume.pdf',
      chokantanplus: 'pdf/2026-11-23_chokantanplus.pdf' } },
    { start: '2026-11-30', files: {
      tezukuri: 'pdf/2026-11-30_tezukuri.pdf',
      kantan: 'pdf/2026-11-30_kantan.pdf',
      chokantan: 'pdf/2026-11-30_chokantan.pdf',
      volume: 'pdf/2026-11-30_volume.pdf',
      chokantanplus: 'pdf/2026-11-30_chokantanplus.pdf' } },
    { start: '2026-12-07', files: {
      tezukuri: 'pdf/2026-12-07_tezukuri.pdf',
      kantan: 'pdf/2026-12-07_kantan.pdf',
      chokantan: 'pdf/2026-12-07_chokantan.pdf',
      volume: 'pdf/2026-12-07_volume.pdf',
      chokantanplus: 'pdf/2026-12-07_chokantanplus.pdf' } },
    { start: '2026-12-14', files: {
      tezukuri: 'pdf/2026-12-14_tezukuri.pdf',
      kantan: 'pdf/2026-12-14_kantan.pdf',
      chokantan: 'pdf/2026-12-14_chokantan.pdf',
      volume: 'pdf/2026-12-14_volume.pdf',
      chokantanplus: 'pdf/2026-12-14_chokantanplus.pdf' } }
  ]
};
