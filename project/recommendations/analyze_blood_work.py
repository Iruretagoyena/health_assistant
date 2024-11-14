def analyze_hemoglobin(hemoglobin):
    if hemoglobin < 13.2:
        return "Hemoglobin: Low value detected. Consider increasing iron intake or consulting a healthcare provider."
    elif hemoglobin > 17.1:
        return "Hemoglobin: High value detected. This could indicate dehydration or other health concerns. Consult a healthcare provider."
    else:
        return "Hemoglobin: Within optimal range. Maintain a balanced diet to support healthy levels."

def analyze_hematocrit(hematocrit):
    if hematocrit < 38.5:
        return "Hematocrit: Low value detected. This may indicate anemia. Consider iron supplementation or dietary adjustments."
    elif hematocrit > 50:
        return "Hematocrit: High value detected. This could be due to dehydration or other health issues. Consider consulting a healthcare provider."
    else:
        return "Hematocrit: Within optimal range. Keep up the healthy habits."

def analyze_mean_cell_hemoglobin(mean_cell_hemoglobin):
    if mean_cell_hemoglobin < 27:
        return "Mean Cell Hemoglobin: Low value detected. This could indicate iron deficiency. Consult with a healthcare provider."
    elif mean_cell_hemoglobin > 33:
        return "Mean Cell Hemoglobin: High value detected. Consider further evaluation with a healthcare provider."
    else:
        return "Mean Cell Hemoglobin: Within optimal range. Maintain your current health practices."

def analyze_mean_cell_hemoglobin_concentration(mean_cell_hemoglobin_concentration):
    if mean_cell_hemoglobin_concentration < 32:
        return "Mean Cell Hemoglobin Concentration: Low value detected. Consider iron-rich foods or supplements."
    elif mean_cell_hemoglobin_concentration > 36:
        return "Mean Cell Hemoglobin Concentration: High value detected. Consult a healthcare provider for further advice."
    else:
        return "Mean Cell Hemoglobin Concentration: Within optimal range. Keep up your healthy habits."

def analyze_mean_cell_volume(mean_cell_volume):
    if mean_cell_volume < 80:
        return "Mean Cell Volume: Low value detected. This could indicate iron deficiency. Consider iron-rich foods or consulting a healthcare provider."
    elif mean_cell_volume > 93.6:
        return "Mean Cell Volume: High value detected. This may suggest a vitamin B12 or folate deficiency. Consider dietary adjustments."
    else:
        return "Mean Cell Volume: Within optimal range. Continue with a balanced diet."

def analyze_red_blood_cells(red_blood_cells):
    if red_blood_cells < 4.2:
        return "Red Blood Cells: Low count detected. Consider iron supplementation or consulting a healthcare provider."
    elif red_blood_cells > 5.8:
        return "Red Blood Cells: High count detected. Monitor hydration levels and consult a healthcare provider if necessary."
    else:
        return "Red Blood Cells: Within optimal range. Maintain your current health practices."

def analyze_basophils(basophils):
    if basophils > 0.2:
        return "Basophils: High value detected. Consider consulting with a healthcare provider to understand the cause."
    else:
        return "Basophils: Within optimal range."

def analyze_eosinophils(eosinophils):
    if eosinophils > 0.5:
        return "Eosinophils: High value detected. This may indicate an allergic response or infection. Consult a healthcare provider."
    else:
        return "Eosinophils: Within optimal range."

def analyze_lymphocytes(lymphocytes):
    if lymphocytes < 0.85:
        return "Lymphocytes: Low value detected. This may indicate a weakened immune response."
    elif lymphocytes > 3.9:
        return "Lymphocytes: High value detected. This may indicate an infection or immune response. Consult a healthcare provider."
    else:
        return "Lymphocytes: Within optimal range."

def analyze_monocytes(monocytes):
    if monocytes < 0.2:
        return "Monocytes: Low value detected. This may be due to stress or immune suppression."
    elif monocytes > 0.95:
        return "Monocytes: High value detected. This may indicate inflammation or infection."
    else:
        return "Monocytes: Within optimal range."

def analyze_neutrophils(neutrophils):
    if neutrophils < 1.5:
        return "Neutrophils: Low value detected. This may increase susceptibility to infections. Consult a healthcare provider."
    elif neutrophils > 7.8:
        return "Neutrophils: High value detected. This could indicate infection or inflammation. Consult a healthcare provider."
    else:
        return "Neutrophils: Within optimal range."

def analyze_white_blood_cells(white_blood_cells):
    if white_blood_cells < 3.8:
        return "White Blood Cells: Low value detected. This could increase infection risk."
    elif white_blood_cells > 10.8:
        return "White Blood Cells: High value detected. This may indicate infection or inflammation. Consult a healthcare provider."
    else:
        return "White Blood Cells: Within optimal range."

def analyze_platelets(platelets):
    if platelets < 140:
        return "Platelets: Low count detected. Monitor for bruising or bleeding."
    elif platelets > 400:
        return "Platelets: High count detected. This may increase the risk of clotting. Consult a healthcare provider."
    else:
        return "Platelets: Within optimal range."

def analyze_ferritin(ferritin):
    if ferritin < 38:
        return "Ferritin: Low value detected. Consider iron supplementation."
    elif ferritin > 380:
        return "Ferritin: High value detected. Monitor for iron overload and consult a healthcare provider."
    else:
        return "Ferritin: Within optimal range."

def analyze_total_cholesterol(total_cholesterol):
    if total_cholesterol > 200:
        return "Total Cholesterol: High value detected. Consider dietary adjustments and physical activity."
    else:
        return "Total Cholesterol: Within optimal range."

def analyze_ldl_cholesterol(ldl_cholesterol):
    if ldl_cholesterol > 100:
        return "LDL Cholesterol: High value detected. Aim to lower LDL through diet and lifestyle adjustments."
    else:
        return "LDL Cholesterol: Within optimal range."

def analyze_hdl_cholesterol(hdl_cholesterol):
    if hdl_cholesterol < 40:
        return "HDL Cholesterol: Low value detected. Consider increasing activity or healthy fat intake."
    else:
        return "HDL Cholesterol: Within optimal range."

def analyze_triglycerides(triglycerides):
    if triglycerides > 150:
        return "Triglycerides: High value detected. Consider reducing sugar and fat intake."
    else:
        return "Triglycerides: Within optimal range."

def analyze_glucose(glucose):
    if glucose < 65:
        return "Glucose: Low value detected. Monitor for symptoms of hypoglycemia."
    elif glucose > 99:
        return "Glucose: Elevated level detected. Consult a healthcare provider to assess risk of diabetes."
    else:
        return "Glucose: Within optimal range."

def analyze_hba1c(hba1c):
    if hba1c > 5.7:
        return "HbA1c: Elevated level detected. Consider lifestyle changes to reduce diabetes risk."
    else:
        return "HbA1c: Within optimal range."

def analyze_creatinine(creatinine):
    if creatinine < 0.6:
        return "Creatinine: Low value detected. Could indicate muscle loss or other concerns."
    elif creatinine > 1.24:
        return "Creatinine: High value detected. Monitor kidney function and consult a healthcare provider."
    else:
        return "Creatinine: Within optimal range."
