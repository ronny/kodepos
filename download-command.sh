seq 1 3402 | ( while read page; do wget -c "http://kodepos.posindonesia.co.id/index.php?act=searchadv&PageNo=$page&kw=%25%25%25&f=35&w=(Semua)&k=sebagian&t=%%%%" -O page-$page.html ; done )
