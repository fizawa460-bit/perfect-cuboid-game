import os
from pathlib import Path
p=Path(os.environ['SRC']); s=p.read_text(); mode=os.environ['MODE']
assert mode in {'pair-capcap','triple-cap','triple-sym','triple-mixed'}
old='''    uint64_t exact_prune_checks_=0,constraint_prunes_=0,exact_symmetry_prune_checks_=0,symmetry_prunes_=0;\n'''
new=old+'''    uint64_t higher_active_checks_=0,higher_active_prunes_=0;\n'''
assert s.count(old)==1; s=s.replace(old,new,1)
anchor='''    bool is_canonical(const std::array<unsigned char,140>& pairing)const{\n'''
fn=r'''    struct HigherCand { int type; int r; int sign; long double severity; };
    cpp_rational hc_center(const HigherCand& c,int last_remaining) {
        if(c.type==0){
            cpp_rational x=exact_center(p_.p0[c.r],cap_a_[c.r],last_remaining);
            return c.sign>0?x:cpp_rational(p_.cap[c.r])-x;
        }
        return exact_center(s_.c0[c.r],sym_a_[c.r],last_remaining);
    }
    cpp_rational hc_coeff(const HigherCand& c,int j) const {
        if(c.type==0) return cpp_rational(c.sign)*cap_a_[c.r][j];
        return sym_a_[c.r][j];
    }
    cpp_rational hc_gram(const HigherCand& a,const HigherCand& b,int last_remaining) const {
        cpp_rational g=0;
        for(int j=0;j<=last_remaining;j++) g+=hc_coeff(a,j)*hc_coeff(b,j)/D_[j];
        return g;
    }
    static cpp_rational det3(const cpp_rational&a,const cpp_rational&b,const cpp_rational&c,
                             const cpp_rational&d,const cpp_rational&e,const cpp_rational&f,
                             const cpp_rational&g,const cpp_rational&h,const cpp_rational&i){
        return a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g);
    }
    bool higher_active_possible(int last_remaining,const cpp_rational& budget) {
        if(last_remaining<0 || budget<=0 || last_remaining>20) return true;
        const long double bf=std::max<long double>(0,budget.convert_to<long double>());
        std::vector<HigherCand> caps,syms,all;
        for(int r=0;r<m_;r++){
            long double center=static_cast<long double>(p_.p0[r])+cap_assignedf_[r];
            long double dist=0; int sign=0;
            if(center<0){dist=-center;sign=1;} else if(center>static_cast<long double>(p_.cap[r])){dist=center-static_cast<long double>(p_.cap[r]);sign=-1;} else continue;
            long double dual=cap_dualf_[r][last_remaining]; if(dual<=0) continue;
            long double reach=std::sqrt(std::max<long double>(0,bf*dual)); if(reach<=0) continue;
            long double sev=dist/reach; if(sev>0.40L) caps.push_back({0,r,sign,sev});
        }
        for(int r=0;r<s_.k;r++){
            long double center=static_cast<long double>(s_.c0[r])+sym_assignedf_[r]; if(center>=0) continue;
            long double dual=sym_dualf_[r][last_remaining]; if(dual<=0) continue;
            long double reach=std::sqrt(std::max<long double>(0,bf*dual)); if(reach<=0) continue;
            long double sev=(-center)/reach; if(sev>0.40L) syms.push_back({1,r,1,sev});
        }
        auto cmp=[](const HigherCand&a,const HigherCand&b){return a.severity==b.severity?(a.type==b.type?a.r<b.r:a.type<b.type):a.severity>b.severity;};
        std::sort(caps.begin(),caps.end(),cmp); std::sort(syms.begin(),syms.end(),cmp);
        if(caps.size()>5)caps.resize(5); if(syms.size()>5)syms.resize(5);
        if(std::string("MODE_PLACEHOLDER")=="pair-capcap"){
            if(caps.size()>4)caps.resize(4);
            for(size_t x=0;x<caps.size();x++) for(size_t y=x+1;y<caps.size();y++){
                ++higher_active_checks_; auto a=caps[x],b=caps[y]; cpp_rational h1=hc_center(a,last_remaining),h2=hc_center(b,last_remaining); if(h1>=0||h2>=0)continue;
                cpp_rational d1=-h1,d2=-h2,g11=hc_gram(a,a,last_remaining),g22=hc_gram(b,b,last_remaining),g12=hc_gram(a,b,last_remaining),det=g11*g22-g12*g12; if(det<=0)continue;
                cpp_rational l1=(d1*g22-d2*g12)/det,l2=(d2*g11-d1*g12)/det; if(l1<=0||l2<=0)continue; if(d1*l1+d2*l2>budget){++higher_active_prunes_;return false;}
            }
            return true;
        }
        if(std::string("MODE_PLACEHOLDER")=="triple-cap") all=caps;
        else if(std::string("MODE_PLACEHOLDER")=="triple-sym") all=syms;
        else { all=caps; all.insert(all.end(),syms.begin(),syms.end()); std::sort(all.begin(),all.end(),cmp); if(all.size()>6)all.resize(6); }
        for(size_t x=0;x<all.size();x++) for(size_t y=x+1;y<all.size();y++) for(size_t z=y+1;z<all.size();z++){
            if(std::string("MODE_PLACEHOLDER")=="triple-mixed") { int t=all[x].type+all[y].type+all[z].type; if(t==0||t==3)continue; }
            ++higher_active_checks_; auto A=all[x],B=all[y],C=all[z]; cpp_rational h1=hc_center(A,last_remaining),h2=hc_center(B,last_remaining),h3=hc_center(C,last_remaining); if(h1>=0||h2>=0||h3>=0)continue;
            cpp_rational d1=-h1,d2=-h2,d3=-h3;
            cpp_rational a=hc_gram(A,A,last_remaining),b=hc_gram(A,B,last_remaining),c=hc_gram(A,C,last_remaining),e=hc_gram(B,B,last_remaining),f=hc_gram(B,C,last_remaining),i=hc_gram(C,C,last_remaining);
            cpp_rational det=det3(a,b,c,b,e,f,c,f,i); if(det<=0)continue;
            cpp_rational n1=det3(d1,b,c,d2,e,f,d3,f,i),n2=det3(a,d1,c,b,d2,f,c,d3,i),n3=det3(a,b,d1,b,e,d2,c,f,d3);
            cpp_rational l1=n1/det,l2=n2/det,l3=n3/det; if(l1<=0||l2<=0||l3<=0)continue;
            if(d1*l1+d2*l2+d3*l3>budget){++higher_active_prunes_;return false;}
        }
        return true;
    }

'''.replace('MODE_PLACEHOLDER',mode)
assert s.count(anchor)==1; s=s.replace(anchor,fn+anchor,1)
s=s.replace('if(caps_possible(n_-1,cpp_rational(bound_)) && symmetry_possible(n_-1,cpp_rational(bound_))) dfs(n_-1,cpp_rational(0));','if(caps_possible(n_-1,cpp_rational(bound_)) && symmetry_possible(n_-1,cpp_rational(bound_)) && higher_active_possible(n_-1,cpp_rational(bound_))) dfs(n_-1,cpp_rational(0));',1)
s=s.replace('if(caps_possible(i-1,newrem) && symmetry_possible(i-1,newrem)){','if(caps_possible(i-1,newrem) && symmetry_possible(i-1,newrem) && higher_active_possible(i-1,newrem)){',1)
meta='''        f<<"  \\\"exact_symmetry_prunes\\\": "<<symmetry_prunes_<<",\\n";\n'''
add=meta+f'''        f<<"  \\\"higher_active_mode\\\": \\\"{mode}\\\",\\n";\n        f<<"  \\\"higher_active_checks\\\": "<<higher_active_checks_<<",\\n";\n        f<<"  \\\"higher_active_prunes\\\": "<<higher_active_prunes_<<",\\n";\n'''
assert s.count(meta)==1; s=s.replace(meta,add,1)
p.write_text(s)
