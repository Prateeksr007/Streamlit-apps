#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import streamlit as st


# In[2]:


st.title('Your Ultimate Tax Calculation Tool')
st.caption('Easily compare the old and new tax regimes to determine which one benefits you the most, ensuring you make the best financial decision')

def old_taxcalculation(old_sal):
    brackets_a = 250000
    brackets_b = 500000
    brackets_c = 100000
    bracket_bmax = 12500
    bracket_cmax = 100000
    if old_sal <= 250000:
        old_tax = 0
    if old_sal > 250000 and old_sal <=500000 :
        old_sal_cal = old_sal -250000 
        old_tax = .05 * old_sal_cal
    if old_sal > 500000 and old_sal <=1000000 :
        old_sal_cal = old_sal -500000
        old_tax = bracket_bmax + (.2 * old_sal_cal)
    else:
        old_sal_cal = old_sal - 1000000
        old_tax = bracket_bmax + bracket_cmax + (.3 * old_sal_cal)
    return(old_tax)
    
def new_taxcalculation(new_sal):
    newbrackets_a = 400000
    newbrackets_b = 800000
    newbrackets_c = 1200000
    newbrackets_d = 1600000
    newbrackets_e = 2000000
    newbrackets_f = 2400000
    newbracket_bmax = 20000
    newbracket_cmax = 40000
    newbracket_dmax = 60000
    newbracket_emax = 80000
    newbracket_fmax = 100000
    
    if new_sal <= 1200000 :
        new_tax = 0
    else:
        if new_sal >1200000 and new_sal <= 1270588 :
            new_tax = new_sal - 1200000
        if new_sal > 1270588 and new_sal <= 1600000 :
            new_sal_cal = new_sal - 1200000
            new_tax = newbracket_bmax + newbracket_cmax + (.15 * new_sal_cal)
        if new_sal > 1600000 and new_sal <= 2000000 :
            new_sal_cal = new_sal - 1600000
            new_tax = newbracket_bmax + newbracket_cmax + newbracket_dmax + (.20 * new_sal_cal)
        if new_sal > 2000000 and new_sal <= 2400000 :
            new_sal_cal = new_sal - 2000000
            new_tax = newbracket_bmax + newbracket_cmax + newbracket_dmax + newbracket_emax + (.25 * new_sal_cal)
        if new_sal > 2400000 :
            new_sal_cal = new_sal - 2400000
            new_tax = newbracket_bmax + newbracket_cmax + newbracket_dmax + newbracket_emax + newbracket_fmax + (.30 * new_sal_cal)
            
    return(new_tax)   
    

#Gross Salary Section
name = st.text_input("Enter your Name",value=None, placeholder="Type your name..." )
salary = st.number_input("Enter your salary", value=None, placeholder="please enter the salary here...")
if name and salary:
    st.write("Hello ", name, ", Your Salary is Rs ", float("{:.2f}".format(salary)))
    st.divider()
    with st.expander("**Declare your Investments in this Section**"):
        st.caption("Please provide the details of your investments here. Based on this information, we will determine which tax regime is most beneficial for you.")
        hra = st.number_input("Enter HRA amount Section 10(13A) (Annually)", placeholder="please enter the amount here...")
        hl = st.number_input("Total Home Loan Interest Amount Section 24(B) (Annually)", placeholder="please enter the amount here...")
        Edl = st.number_input("Education Loan Interest Amount Section 80(E) (Annually)", placeholder="please enter the amount here...")
        don = st.number_input("Donation Amount to political parties Section 80(G) (Annually) ", placeholder="please enter the amount here...")
        sec80 = st.slider("Total Investments under Section 80(C) (Annually)", 0,150000,100000 )
        st.caption("Maximum deduction allowed up to ₹1,50,000")
        nps = st.slider("NPS Investment under Section 80 CCD(1B) (Annually)", 0,50000,0)
        st.caption("Maximum deduction allowed up to ₹50,000")
        ins = st.slider("Health Insurance Amount 80(D) (Self + Senior Citizens) (Annually)",0,75000,25000)
        st.caption("Maximum deduction allowed up to ₹75,000 (Self - ₹25,000 & Senior Citizens - ₹50,000)")

    st.divider()
    #Two Sections Old and New Tax Regime
    cols = st.columns([1, 1])

    #Old Tax Regime
    with cols[0]:
        with st.container(border=True):
            st.write("**Tax Calculation Based on Old Regime**")
            st.divider()
            #old_nettaxable_salary = salary - (50000+hra+Edl+nps+sec80+ins+don+hl)
            with st.expander("**Total Applicable Deductions**"):
                st.write("Standard Deduction :",50000)
                st.write("HRA Deduction :",hra)
                st.write("Home Loan Interest Deduction :",hl)
                st.write("Education Loan Interest Deduction :",Edl)
                st.write("NPS Deduction :",nps)
                st.write("Sec80(c) Deduction :",sec80)
                st.write("Insurance Deduction",ins)
                st.write("Donation Amount Deduction",don)
            with st.container(border=True):
                old_nettaxable_salary = salary - (50000+hra+Edl+nps+sec80+ins+don+hl)
                st.write("Taxable Salary :", float("{:.2f}".format(old_nettaxable_salary)))
            with st.container(border=True):
                final_old_tax = old_taxcalculation(old_nettaxable_salary)
                st.write("Tax as per Old Regime :",float("{:.2f}".format(final_old_tax)))


    with cols[1]:
        with st.container(border=True):
            st.write("**Tax Calculation Based on New Regime**")
            st.divider()
            with st.expander("**Total Applicable Deductions**"):
                st.write("Standard Deduction :",75000)
            with st.container(border=True):
                new_nettaxable_salary = salary-75000
                st.write("Taxable Salary :", float("{:.2f}".format(new_nettaxable_salary)))
            with st.container(border=True):
                final_new_tax = new_taxcalculation(new_nettaxable_salary)
                st.write("Tax as per New Regime :",float("{:.2f}".format(final_new_tax)))
    
    st.divider()
    st.write("**Which Tax Regime to choose**")
    st.caption("Please note that I have not accounted for education cess, employee and employer provident fund contributions, or income from other sources.")
    with st.container(border=True):
        if final_new_tax > final_old_tax :
            st.markdown(f'<p style="color:green; font-weight:normal;">{name} - You should choose Old Tax Regime</p>', unsafe_allow_html=True)
            s = (final_new_tax - final_old_tax)*100/final_new_tax
            st.write("You pay tax ₹", float("{:.2f}".format(final_old_tax))," which is ",float("{:.2f}".format(s)),"% lower than the New tax")
            st.write("You save ₹", float("{:.2f}".format(final_new_tax - final_old_tax)), "in comparison to new tax regime")
            st.write("Your annual take-home salary post taxes is ₹", float("{:.2f}".format(salary - final_old_tax)))
            inhand = (salary - final_old_tax)/12
            #st.write("Your monthly take-home salary post taxes is ₹", float("{:.2f}".format(inhand)))
        
        else:
            st.markdown(f'<p style="color:green; font-weight:normal;">{name} - You should choose New Tax Regime</p>', unsafe_allow_html=True)
            s = (final_old_tax - final_new_tax)*100/final_old_tax
            if final_new_tax == final_old_tax :
                st.write("As you have less complexities in New Tax Regime ")
                st.write("Your annual take-home salary post taxes is ₹", float("{:.2f}".format(salary - final_new_tax)))
                inhand = (salary - final_new_tax)/12
                #st.write("Your monthly take-home salary post taxes is ₹", float("{:.2f}".format(inhand)))
            else:
                st.write("You pay tax ₹", float("{:.2f}".format(final_new_tax))," which is ",float("{:.2f}".format(s)),"% lower than the Old tax")
                st.write("You save ₹", float("{:.2f}".format(final_old_tax - final_new_tax)), "in comparison to old tax regime")
                st.write("Your annual take-home salary post taxes is ₹", float("{:.2f}".format(salary - final_new_tax)))
                inhand = (salary - final_new_tax)/12
                #st.write("Your monthly take-home salary post taxes is ₹", float("{:.2f}".format(inhand)))
    
    #st.markdown('<p style="position:fixed; bottom:0; width:100%; text-align:centre;">Prateek Singh Rathore</p>', unsafe_allow_html=True)
    st.divider()
    st.markdown('<div style="text-align:right; margin-top:50px;">Prateek Singh Rathore</div>', unsafe_allow_html=True)
    


# In[ ]:




