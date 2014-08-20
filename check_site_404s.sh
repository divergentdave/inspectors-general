#!/bin/sh

function get_http_code() {
  echo -n "${1:0:30}... "
  curl -ISs "$1" | head -n 1
}

get_http_code http://www.usda.gov/oig/doesyour404work
get_http_code http://amtrakoig.gov/doesyour404work
get_http_code http://www.arc.gov/oig/doesyour404work
get_http_code http://www.archives.gov/oig/doesyour404work
get_http_code http://www.cftc.gov/About/OfficeoftheInspectorGeneral/doesyour404work
get_http_code http://www.cncsoig.gov/doesyour404work
get_http_code http://www.oig.doc.gov/doesyour404work
get_http_code http://www.cpb.org/oig/doesyour404work
get_http_code https://www.cpsc.gov/en/about-cpsc/inspector-general/doesyour404work
get_http_code http://www.oig.denali.gov/doesyour404work
get_http_code http://www.oig.dhs.gov/doesyour404work
get_http_code http://www.dodig.mil/doesyour404work
get_http_code http://www.justice.gov/oig/reports/doesyour404work
get_http_code https://www.oig.dot.gov/doesyour404work
get_http_code http://www.eac.gov/inspector_general/doesyour404work
get_http_code https://www2.ed.gov/about/offices/list/oig/doesyour404work
get_http_code http://www.eeoc.gov/eeoc/oig/doesyour404work
get_http_code http://energy.gov/ig/office-inspector-general/doesyour404work
get_http_code http://www.epa.gov/oig/doesyour404work
get_http_code http://www.exim.gov/oig/doesyour404work
get_http_code https://www.fca.gov/home/doesyour404work
get_http_code http://fcc.gov/oig/doesyour404work
get_http_code http://www.fdicoig.gov/doesyour404work
get_http_code http://www.fec.gov/fecig/doesyour404work
get_http_code http://oig.federalreserve.gov/doesyour404work
get_http_code http://fhfaoig.gov/doesyour404work
get_http_code https://www.flra.gov/OIG/doesyour404work
get_http_code http://www.fmc.gov/bureaus_offices/doesyour404work
get_http_code http://www.ftc.gov/about-ftc/office-inspector-general/doesyour404work
get_http_code http://www.gao.gov/about/workforce/doesyour404work
get_http_code http://www.gpo.gov/oig/doesyour404work
get_http_code http://gsaig.gov/doesyour404work
get_http_code https://oig.hhs.gov/doesyour404work
get_http_code http://house.gov/content/learn/officers_and_organizations/inspector_general/doesyour404work
get_http_code http://www.hudoig.gov/doesyour404work
get_http_code http://www.doi.gov/oig/doesyour404work
get_http_code http://www.usitc.gov/oig/doesyour404work
get_http_code http://www.oig.dol.gov/doesyour404work
get_http_code http://www.loc.gov/about/office-of-the-inspector-general/doesyour404work
get_http_code http://www.oig.lsc.gov/doesyour404work
get_http_code http://oig.nasa.gov/doesyour404work
get_http_code http://www.ncua.gov/about/Leadership/Pages/doesyour404work
get_http_code http://arts.gov/oig/doesyour404work
get_http_code http://www.neh.gov/about/oig/doesyour404work
get_http_code https://www.nlrb.gov/who-we-are/inspector-general/doesyour404work
get_http_code http://www.nrc.gov/doesyour404work
get_http_code https://www.nsf.gov/oig/doesyour404work
get_http_code https://www.opm.gov/our-inspector-general/doesyour404work
get_http_code http://oig.pbgc.gov/doesyour404work
get_http_code http://www.peacecorps.gov/about/inspgen/doesyour404work
get_http_code http://www.prc.gov/prc-pages/about/offices/doesyour404work
get_http_code http://www.rrb.gov/oig/doesyour404work
get_http_code http://www.sba.gov/office-of-inspector-general/doesyour404work
get_http_code http://www.sec.gov/about/offices/oig/doesyour404work
get_http_code http://www.si.edu/OIG/doesyour404work
get_http_code http://www.sigar.mil/doesyour404work
get_http_code http://www.sigtarp.gov/doesyour404work
get_http_code http://oig.ssa.gov/doesyour404work
get_http_code http://oig.state.gov/doesyour404work
get_http_code http://www.treasury.gov/tigta/doesyour404work
get_http_code http://www.treasury.gov/about/organizational-structure/ig/doesyour404work
get_http_code http://oig.tva.gov/doesyour404work
get_http_code https://oig.usaid.gov/doesyour404work
get_http_code https://uspsoig.gov/doesyour404work
get_http_code http://www.va.gov/oig/doesyour404work
