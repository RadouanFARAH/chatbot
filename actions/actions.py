# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
import datetime
from rasa_sdk.events import AllSlotsReset,UserUtteranceReverted
import re
import mysql.connector 
from rasa_sdk.events import SlotSet, ActiveLoop, LoopInterrupted,Restarted
from rasa_sdk.executor import CollectingDispatcher
from math import floor, ceil
import math

variable_globale=""
id_demande=0

flag_type_local=0

class Action_offre_souhaitez(Action):

     def name(self) -> Text:
         return "action_offre_souhaitez"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
         offre=tracker.get_slot("offre_souhaitez")
         
         if(not offre):
             dispatcher.utter_message(response="utter_pardon")
             #dispatcher.utter_RTmoumtaz
         elif(offre.lower()=="moumtaz"):
             dispatcher.utter_message(response = "utter_RTmoumtaz")
         elif(offre.lower()=="tanmiya"):
             dispatcher.utter_message(response = "utter_RTtanmiya")
         elif(offre.lower()=="oto"):
             dispatcher.utter_message(response = "utter_RToto")
         elif(offre.lower()=="milkia"):
             dispatcher.utter_message(response = "utter_RTmilkia")
         elif(offre.lower()=="pret individuel au logement" or offre.lower()=="pret individuel logement" or offre.lower()=="pil"):
             dispatcher.utter_message(response="utter_RPIL")
         elif(offre.lower()=="pret individuel à l'entreprise" or offre.lower()=="pret individuel entreprise" or offre.lower()=="pie"):
             dispatcher.utter_message(response="utter_RPIE")
         elif(offre.lower()=="pret solidaire"  or offre.lower()=="ps"):
             dispatcher.utter_message(response="utter_RPS")
    

         return []




class Action_condition_offre(Action):

     def name(self) -> Text:
         return "action_condition_offre"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
         offre=tracker.get_slot("offre_souhaitez")
        
         if(not offre):
             dispatcher.utter_message(response="utter_pardon")
             #dispatcher.utter_RTmoumtaz
         elif(offre.lower()=="moumtaz"):
             dispatcher.utter_message(response = "utter_RCondition_TM")
         elif(offre.lower()=="tanmiya"):
             dispatcher.utter_message(response = "utter_RCondition_TT")
         elif(offre.lower()=="oto"):
             dispatcher.utter_message(response = "utter_RCondition_TOto")
         elif(offre.lower()=="milkia"):
             dispatcher.utter_message(response = "utter_RCondition_TMilkia")
         elif(offre.lower()=="pret individuel au logement" or offre.lower()=="pret individuel logement" or offre.lower()=="pil"):
             dispatcher.utter_message(response="utter_RCondition_PIL")
         elif(offre.lower()=="pret individuel à l'entreprise" or offre.lower()=="pret individuel entreprise" or offre.lower()=="pie"):
             dispatcher.utter_message(response="utter_RCondition_PIE")
         elif(offre.lower()=="pret solidaire"  or offre.lower()=="ps"):
             dispatcher.utter_message(response="utter_RCondition_PS")
    

         return []


class Action_utilisation_offre(Action):

     def name(self) -> Text:
         return "action_utilisation_offre"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
         offre=tracker.get_slot("offre_souhaitez")
        
         if(not offre):
             dispatcher.utter_message(response="utter_pardon")
             #dispatcher.utter_RTmoumtaz
         elif(offre.lower()=="moumtaz"):
             dispatcher.utter_message(response = "utter_R_utilisation_moumtaz")
         elif(offre.lower()=="tanmiya"):
             dispatcher.utter_message(response = "utter_R_utilisation_tanmiya")
         elif(offre.lower()=="oto"):
             dispatcher.utter_message(response = "utter_R_utilisation_oto")
         elif(offre.lower()=="milkia"):
             dispatcher.utter_message(response = "utter_R_utilisation_milkia")
         elif(offre.lower()=="pret individuel au logement" or offre.lower()=="pret individuel logement" or offre.lower()=="pil"):
             dispatcher.utter_message(response="utter_R_utilisation_PIL")
         elif(offre.lower()=="pret individuel à l'entreprise" or offre.lower()=="pret individuel entreprise" or offre.lower()=="pie"):
             dispatcher.utter_message(response="utter_R_utilisation_PIE")
         elif(offre.lower()=="pret solidaire"  or offre.lower()=="ps"):
             dispatcher.utter_message(response="utter_R_utilisation_PS")

         return []


class Action_garanties_offre(Action):

     def name(self) -> Text:
         return "action_garanties_offre"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
         offre=tracker.get_slot("offre_souhaitez")
        
         if(not offre):
             dispatcher.utter_message(response="utter_pardon")
             #dispatcher.utter_RTmoumtaz
         elif(offre.lower()=="moumtaz"):
             dispatcher.utter_message(response = "utter_R_garanties_moumtaz")
         elif(offre.lower()=="tanmiya"):
             dispatcher.utter_message(response = "utter_R_garanties_tanmiya")
         elif(offre.lower()=="oto"):
             dispatcher.utter_message(response = "utter_R_garanties_oto")
         elif(offre.lower()=="milkia"):
             dispatcher.utter_message(response = "utter_r_garanties_milkia")
         elif(offre.lower()=="pret individuel au logement" or offre.lower()=="pret individuel logement" or offre.lower()=="pil"):
             dispatcher.utter_message(response="utter_R_garanties_PIL")
         elif(offre.lower()=="pret individuel à l'entreprise" or offre.lower()=="pret individuel entreprise" or offre.lower()=="pie"):
             dispatcher.utter_message(response="utter_R_garanties_PIE")
         elif(offre.lower()=="pret solidaire"  or offre.lower()=="ps"):
             dispatcher.utter_message(response="utter_R_garanties_PS")
         return []
     


class Action_offre_non_financier(Action):

     def name(self) -> Text:
         return "action_offre_non_financier"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        
         intent=tracker.get_intent_of_latest_message()
         
         if(intent=="offre_non_F_1"):
             dispatcher.utter_message(response="utter_R_offre_AF")
         elif(intent=="offre_non_F_2"):
             dispatcher.utter_message(response="utter_R_offre_AC")
         elif(intent=="offre_non_F_3"):
             dispatcher.utter_message(response="utter_R_offre_PC")
         
         return []



class ActionResetAllSlots(Action):

    def name(self):

        return "action_reset_all_slots"

    def run(self, dispatcher, tracker, domain):
        global flag_type_local
        flag_type_local=0
        return [AllSlotsReset()]
    

def clean_name(name):
    return "".join([c for c in name if c.isalpha()])

class ValidateIdentificationForm(FormValidationAction):
    
    def name(self) -> Text:
        return "validate_indentification_form"


class Aherche_adresse_agence(Action):

    def name(self) -> Text:
        return "action_ask_adresse_a"

    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         
         msg=tracker.latest_message.get("text")
         msg=msg.lower()
         intent=tracker.get_intent_of_latest_message()

         if(intent=="A_ville" or intent=="A_quartier"):
             
             global variable_globale
             variable_globale = str(msg)

             db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="chatbot_database"
            )

             cursor = db.cursor()
            
             query1="SELECT agence,adresse,ville FROM agences"
             

             l=[]
             #l.append("%"+msg+"%")
             params = (l)

             cursor.execute(query1, params)
             results = cursor.fetchall()
             i=0
             if(len(results)!=0):
                
                for row in results:
                    
                    agence=row[0]
                    adresse=row[1]
                    ville=row[2]

                    if(round(jaro_distance(adresse.lower(),msg),6)*100 >= 80 or  round(jaro_distance(ville.lower(),msg),6)*100 >= 80):
                        if(i==0):
                            dispatcher.utter_message(text="Voila la liste des agences dans votre Zone")
                            i=1
                        dispatcher.utter_message(text="Agence: "+str(agence)+"&Ville :"+str(ville)+"&Adresse: "+str(adresse))
                if(i==1):
                    db.close()
                    return[Restarted()]
                else:
                    dispatcher.utter_message(text="merci de saisir la ville ou le quartier")
                    return []
         else: 
             dispatcher.utter_message(text="merci de saisir la ville ou le quartier")
             return []
          
         
             

class Validatecherche_agence(FormValidationAction):
    
    def name(self) -> Text:
        return "validate_cherche_agence"

    def validate_adresse_a(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker:Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        msg=tracker.latest_message.get("text")
        msg=msg.lower()
        intent=tracker.get_intent_of_latest_message()

        ###########################
        

        
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="chatbot_database"
            )

        cursor = db.cursor()

        query1="SELECT agence,adresse,ville FROM agences"

        l=[]
        #l.append("%"+msg+"%")
        params = (l)

        cursor.execute(query1, params)
        results = cursor.fetchall()
        i=0
        if(len(results)!=0):
            
            for row in results:
                    
                    agence=row[0]
                    adresse=row[1]
                    ville=row[2]

                    if(round(jaro_distance(adresse.lower(),msg),6)*100 >= 80  or  round(jaro_distance(ville.lower(),msg),6)*100 >= 80):
                        if(i==0):
                            dispatcher.utter_message(text="Voila la liste des agences dans votre Zone")
                            i=1
                        dispatcher.utter_message(text="Agence: "+str(agence)+"&Ville :"+str(ville)+"&Adresse: "+str(adresse))
            
            if(i==1):
                db.close()
                return {"adresse_a":True}
            elif(i==0):
             
             
                for row in results:
                    
                    agence=row[0]
                    adresse=row[1]
                    ville=row[2]
                    
                    nombre_espace=adresse.count(" ")
                    k=1
                    while(k<=nombre_espace):

                        result=split_adresse(adresse,k)

                        if(round(jaro_distance(result[0].lower(),msg),6)*100 >= 80  or  round(jaro_distance(result[1].lower(),msg),6)*100 >= 80):
                            if(i==0):
                                dispatcher.utter_message(text="Voila l'agence la plus proche pour vous")
                                i=3
                            dispatcher.utter_message(text="Agence: "+str(agence)+"&Ville :"+str(ville)+"&Adresse: "+str(adresse))
                            break
                        k=k+1
                    if(i==3):
                        break
                
                if(i==3):
                    return{'adresse_a':True}
                
                dispatcher.utter_message(text="Si vous êtes sûr des informations que vous avez fournies. alors je suis désolé, il n'y a pas d'agence dans votre zone.")
                db.close()
                return{'adresse_a':False}
        
    

    


class Validateform1_form(FormValidationAction):
    
    PM=None
    EI=None
    PP=None
    etat=None
    ex_cal=None
    flag_agence=None

    def name(self) -> Text:
        return "validate_form1_form"

    async def required_slots(
        self,
        domain_slots: List[Text],
        dispatcher: "CollectingDispatcher",
        tracker: "Tracker",
        domain: "DomainDict",
    ) -> List[Text]:
        updated_slots = domain_slots.copy()
        if tracker.slots.get("A_G_revenu") == False:
            updated_slots.remove("six_mois_activite")
            updated_slots.remove("condition")
            updated_slots.remove("type_demande")
            updated_slots.remove("contrat")
            updated_slots.remove("secteur_A")
            updated_slots.remove("activite")
            updated_slots.remove("nom")
            updated_slots.remove("prenom")
            updated_slots.remove("cin")
            updated_slots.remove("adresse")
            updated_slots.remove("ville")
            updated_slots.remove("cherche_agence_2")
            updated_slots.remove("cherche_agence_1")
            updated_slots.remove("agence_plus_proche")
            updated_slots.remove("email")
            updated_slots.remove("numero_telephone")
            updated_slots.remove("date_naissance")
            updated_slots.remove("type_numero")
            updated_slots.remove("numero_RC_patente_ICE")
            updated_slots.remove("nom_entreprise")
            updated_slots.remove("GSME")
            updated_slots.remove("adresse_entreprise")
            updated_slots.remove("ville_entreprise")
            updated_slots.remove("frome_juridique")
            updated_slots.remove("offre")
            updated_slots.remove("montant_souhaite")
            updated_slots.remove("type_locale")
            updated_slots.remove("garantie")
            updated_slots.remove("revenu_mensuel")
            updated_slots.remove("charges_mensuelles")
            updated_slots.remove("charges_familiales")
            updated_slots.remove("excedant")
            updated_slots.remove("autre_revenu")
            updated_slots.remove("autres_pret")
            updated_slots.remove("montant_finale")
            updated_slots.remove("confirmer_demande")
        if tracker.slots.get("six_mois_activite") == False:
            updated_slots.remove("condition")
            updated_slots.remove("type_demande")
            updated_slots.remove("contrat")
            updated_slots.remove("secteur_A")
            updated_slots.remove("activite")
            updated_slots.remove("nom")
            updated_slots.remove("prenom")
            updated_slots.remove("cin")
            updated_slots.remove("adresse")
            updated_slots.remove("ville")
            updated_slots.remove("cherche_agence_2")
            updated_slots.remove("cherche_agence_1")
            updated_slots.remove("agence_plus_proche")
            updated_slots.remove("email")
            updated_slots.remove("numero_telephone")
            updated_slots.remove("date_naissance")
            updated_slots.remove("type_numero")
            updated_slots.remove("numero_RC_patente_ICE")
            updated_slots.remove("nom_entreprise")
            updated_slots.remove("GSME")
            updated_slots.remove("adresse_entreprise")
            updated_slots.remove("ville_entreprise")
            updated_slots.remove("frome_juridique")
            updated_slots.remove("offre")
            updated_slots.remove("montant_souhaite")
            updated_slots.remove("type_locale")
            updated_slots.remove("garantie")
            updated_slots.remove("revenu_mensuel")
            updated_slots.remove("charges_mensuelles")
            updated_slots.remove("charges_familiales")
            updated_slots.remove("excedant")
            updated_slots.remove("autre_revenu")
            updated_slots.remove("autres_pret")
            updated_slots.remove("montant_finale")
            updated_slots.remove("confirmer_demande")
        if tracker.slots.get("condition") == False:
            updated_slots.remove("type_demande")
            updated_slots.remove("contrat")
            updated_slots.remove("secteur_A")
            updated_slots.remove("activite")
            updated_slots.remove("nom")
            updated_slots.remove("prenom")
            updated_slots.remove("cin")
            updated_slots.remove("adresse")
            updated_slots.remove("ville")
            updated_slots.remove("cherche_agence_2")
            updated_slots.remove("cherche_agence_1")
            updated_slots.remove("agence_plus_proche")
            updated_slots.remove("email")
            updated_slots.remove("numero_telephone")
            updated_slots.remove("date_naissance")
            updated_slots.remove("type_numero")
            updated_slots.remove("numero_RC_patente_ICE")
            updated_slots.remove("nom_entreprise")
            updated_slots.remove("GSME")
            updated_slots.remove("adresse_entreprise")
            updated_slots.remove("ville_entreprise")
            updated_slots.remove("frome_juridique")
            updated_slots.remove("offre")
            updated_slots.remove("montant_souhaite")
            updated_slots.remove("type_locale")
            updated_slots.remove("garantie")
            updated_slots.remove("revenu_mensuel")
            updated_slots.remove("charges_mensuelles")
            updated_slots.remove("charges_familiales")
            updated_slots.remove("excedant")
            updated_slots.remove("autre_revenu")
            updated_slots.remove("autres_pret")
            updated_slots.remove("montant_finale")
            updated_slots.remove("confirmer_demande")
        
        
        if tracker.slots.get("contrat") == False:
            
            updated_slots.remove("secteur_A")
            updated_slots.remove("activite")
            updated_slots.remove("nom")
            updated_slots.remove("prenom")
            updated_slots.remove("cin")
            updated_slots.remove("adresse")
            updated_slots.remove("ville")
            updated_slots.remove("cherche_agence_2")
            updated_slots.remove("cherche_agence_1")
            updated_slots.remove("agence_plus_proche")
            updated_slots.remove("email")
            updated_slots.remove("numero_telephone")
            updated_slots.remove("date_naissance")
            updated_slots.remove("type_numero")
            updated_slots.remove("numero_RC_patente_ICE")
            updated_slots.remove("nom_entreprise")
            updated_slots.remove("GSME")
            updated_slots.remove("adresse_entreprise")
            updated_slots.remove("ville_entreprise")
            updated_slots.remove("frome_juridique")
            updated_slots.remove("offre")
            updated_slots.remove("montant_souhaite")
            updated_slots.remove("type_locale")
            updated_slots.remove("garantie")
            updated_slots.remove("revenu_mensuel")
            updated_slots.remove("charges_mensuelles")
            updated_slots.remove("charges_familiales")
            updated_slots.remove("excedant")
            updated_slots.remove("autre_revenu")
            updated_slots.remove("autres_pret")
            updated_slots.remove("montant_finale")
            updated_slots.remove("confirmer_demande")
        if(tracker.get_slot('type_locale')==False):
            updated_slots.remove("garantie")
            updated_slots.remove("revenu_mensuel")
            updated_slots.remove("charges_mensuelles")
            updated_slots.remove("charges_familiales")
            updated_slots.remove("excedant")
            updated_slots.remove("autre_revenu")
            updated_slots.remove("autres_pret")
            updated_slots.remove("montant_finale")
            updated_slots.remove("confirmer_demande")

        if(tracker.get_slot('garantie')==False):
            updated_slots.remove("revenu_mensuel")
            updated_slots.remove("charges_mensuelles")
            updated_slots.remove("charges_familiales")
            updated_slots.remove("excedant")
            updated_slots.remove("autre_revenu")
            updated_slots.remove("autres_pret")
            updated_slots.remove("montant_finale")
            updated_slots.remove("confirmer_demande")

        if(tracker.get_slot('frome_juridique')==False):
            updated_slots.remove("offre")
            updated_slots.remove("montant_souhaite")
            updated_slots.remove("type_locale")
            updated_slots.remove("garantie")
            updated_slots.remove("revenu_mensuel")
            updated_slots.remove("charges_mensuelles")
            updated_slots.remove("charges_familiales")
            updated_slots.remove("excedant")
            updated_slots.remove("autre_revenu")
            updated_slots.remove("autres_pret")
            updated_slots.remove("montant_finale")
            updated_slots.remove("confirmer_demande")
        # if(self.PM==False and self.EI==True and self.PP==False): # cas de EI     ##### cas generale PM
        #     updated_slots.remove("nom_entreprise")                  ####### a vérifier
        if(self.PM==False and self.EI==False and self.PP==True):  # cas de PP
            updated_slots.remove("contrat")
            updated_slots.remove("type_numero")
            updated_slots.remove("numero_RC_patente_ICE")
            updated_slots.remove("frome_juridique")
            updated_slots.remove("nom_entreprise")
            updated_slots.remove("GSME")
            updated_slots.remove("adresse_entreprise")
            updated_slots.remove("ville_entreprise")
        if(self.etat==3):
            updated_slots.remove("autre_revenu")
            updated_slots.remove("autres_pret")
        if(self.etat==1):
            updated_slots.remove("autres_pret")
        if(self.etat==2):
            updated_slots.remove("autre_revenu")
        if(self.etat==-1):
            updated_slots.remove("autre_revenu")
            updated_slots.remove("autres_pret")
            updated_slots.remove("montant_finale")
            updated_slots.remove("confirmer_demande")
        if(self.flag_agence==True):
            updated_slots.remove("cherche_agence_2")
            


        return updated_slots
    

    def validate_A_G_revenu(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker:Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        msg=tracker.latest_message.get("text")
        msg=msg.lower()
        intent=tracker.get_intent_of_latest_message()

        if(intent=="affirmation" or (intent=="chiffre" and msg=="1")):
            return{'A_G_revenu':True}
        elif(intent=="inffirmation" or (intent=="chiffre" and msg=="2")):
            dispatcher.utter_message(response="utter_malheuressement")
            return{'A_G_revenu':False}
        else:
             dispatcher.utter_message(response="utter_pardon")
             return{'A_G_revenu':None}

    
    def validate_six_mois_activite(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker:Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        msg=tracker.latest_message.get("text")
        msg=msg.lower()
        intent=tracker.get_intent_of_latest_message()
        if(intent=="affirmation" or (intent=="chiffre" and msg=="1")):
            return{'six_mois_activite':True}
        elif(intent=="inffirmation" or (intent=="chiffre" and msg=="2")):
            dispatcher.utter_message(response="utter_malheuressement")
            return{'six_mois_activite':False}
        else:
             dispatcher.utter_message(response="utter_pardon")
             return{'six_mois_activite':None}
    
    def validate_condition(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker:Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        msg=tracker.latest_message.get("text")
        msg=msg.lower()
        intent=tracker.get_intent_of_latest_message()

        if(intent=="condition_1" or (intent=="chiffre" and msg=="1")):
            self.PM=True
            self.EI=False
            self.PP=False
            
            return{"condition":"1"}
        elif(intent=="condition_2" or (intent=="chiffre" and msg=="2")):
            self.PM=False
            self.EI=True
            self.PP=False
            
            return{"condition":"2"}
        elif(intent=="condition_3" or (intent=="chiffre" and msg=="3")):
            self.PM=False
            self.EI=True
            self.PP=False
            
            return{"condition":"3"}
        elif(intent=="condition_4" or (intent=="chiffre" and msg=="4")):
            self.PM=False
            self.EI=True
            self.PP=False
            
            return{"condition":"4"}
        elif(intent=="condition_5" or (intent=="chiffre" and msg=="5")):
            self.PM=False
            self.EI=True
            self.PP=False
            
            return{"condition":"5"}
        elif(intent=="condition_6" or (intent=="chiffre" and msg=="6")):
            self.PM=False
            self.EI=True
            self.PP=False
            
            return{"condition":"6"}
        elif(intent=="condition_7" or (intent=="chiffre" and msg=="7")):
            self.PM=False
            self.EI=False
            self.PP=True
            
            return{"condition":"7"}
        elif(intent=="condition_8" or (intent=="chiffre" and msg=="8")):
            self.PM=False
            self.EI=False
            self.PP=True
            
            return{"condition":"8"}
        elif((intent=="inffirmation")):
            dispatcher.utter_message(response="utter_malheuressement")
            return{'condition':False}
        else:
            dispatcher.utter_message(response="utter_pardon")
            return{"condition":None}
        
    
        
    def validate_contrat(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker:Tracker,
        domain: DomainDict,
    )-> Dict[Text, Any]:
        

        msg=tracker.latest_message.get("text")
        msg=msg.lower()
        intent=tracker.get_intent_of_latest_message()

        

        if((intent=="chiffre" and msg=="1") or(intent=="contrat_type_1")):
            
            self.PM=False
            self.EI=False
            self.PP=True
            
            return{'contrat':'au nom du client'}
        
        elif((intent=="chiffre" and msg=="2") or(intent=="contrat_type_2")):
            
            return{"contrat":"au nom d'entreprise"}
        
        elif((intent=="inffirmation")):
            dispatcher.utter_message(response="utter_malheuressement")
            return{'contrat':False}
        else:
            dispatcher.utter_message(response="utter_pardon")
            return{'contrat':None}
         
    def validate_secteur_A(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker:Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        
        
        if(self.PM==True):
            vv="PM"
        elif(self.EI==True):
            vv="EI"
        elif(self.PP==True):
            vv="PP"
        msg=tracker.latest_message.get("text")
        msg=msg.lower()
        intent=tracker.get_intent_of_latest_message()

        if (intent=="secteur_activite"):

            list_secteur_activite=["artisanat","commerce","privé","public","agriculture","service"]
            similarite=0
            
            for se in list_secteur_activite:
                if(round(jaro_distance(se,msg),6)*100 > similarite):
                    similarite=round(jaro_distance(se,msg),6)*100
                    secteur=se
            return {"secteur_A":secteur ,"type_demande":vv}
        
        elif(intent=="chiffre" and msg=="1"):
            return {"secteur_A":'artisanat','type_demande':vv}
        elif(intent=="chiffre" and msg=="2"):
            return {"secteur_A":'commerce','type_demande':vv}
        elif(intent=="chiffre" and msg=="3"):
            return {"secteur_A":'privé','type_demande':vv}
        elif(intent=="chiffre" and msg=="4"):
            return {"secteur_A":'public','type_demande':vv}
        elif(intent=="chiffre" and msg=="5"):
            return {"secteur_A":'agriculture','type_demande':vv}
        elif(intent=="chiffre" and msg=="6"):
            return {"secteur_A":'service','type_demande':vv}
        
        dispatcher.utter_message(response="utter_pardon")
        return {"secteur_A":None}
    
    def validate_activite(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker:Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        
        msg=tracker.latest_message.get("text")
        msg=msg.lower()
        intent=tracker.get_intent_of_latest_message()

        
        
        if (intent=="activite"):

            db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="chatbot_database"
            )

            cursor = db.cursor()

            query1="SELECT code,activite,secteur FROM activite"
            cursor.execute(query1)
            results = cursor.fetchall()
            secteur_a=tracker.get_slot("secteur_A")
            
            if(len(results)!=0):
                
                similarite_valeur=0
                select_code=0
                select_activite=""
                select_secteur=""
                for row in results:
                    
                    code=row[0]
                    activite=row[1]
                    secteur=row[2]

                    if(round(jaro_distance(activite.lower(),msg),6)*100 > similarite_valeur):
                        similarite_valeur=round(jaro_distance(activite.lower(),msg),6)*100
                        select_code=code
                        select_activite=activite
                        select_secteur=secteur
                

                if(secteur_a.lower() != select_secteur.lower()):
                    dispatcher.utter_message(text="Désolé, l'activité que vous avez saisie n'est pas compatible avec votre secteur d'activité")
                    return{"activite":None}
                
                return {"activite":select_code}
        
        dispatcher.utter_message(response="utter_pardon")
        return {"activite":None}
        
    
    def validate_nom(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker:Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        
        
        name=clean_name(slot_value)
        if len(name) <= 2:
            dispatcher.utter_message(text="le Nom saisi est invalide ")
            return {"nom":None}
        return {"nom":name}

    def validate_prenom(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker:Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        
        
        name=clean_name(slot_value)
        if len(name) <= 2:
            dispatcher.utter_message(text="le Prenom saisi est invalide ")
            return {"prenom":None}
        return {"prenom":name}
    
    def validate_cin(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker:Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        
        cin=slot_value
        if verifier_cin(cin) == False:
            dispatcher.utter_message(text="le cin saisi est invalide ")
            return {"cin":None}
        return {"cin":cin}
    
    def validate_adresse(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker:Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        
        adresse=slot_value
        if len(adresse) <= 3:
            dispatcher.utter_message(text="l'adresse saisi est invalide ")
            return {"adresse":None}
        return {"adresse":adresse}
    
    def validate_ville(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker:Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
    
        ville=slot_value
        ville=clean_name(ville)
        

        if(len(ville)<=2):
            dispatcher.utter_message(text="la ville saisi est invalide ")
            return {"ville":None,"cherche_agence_1":None}
        
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="chatbot_database"
            )
        cursor = db.cursor()
        query1="SELECT codeagence,adresse,ville FROM agences"

        cursor.execute(query1)
        results = cursor.fetchall()

        
        adresse=tracker.get_slot('adresse')
        
        similarite_adresse=0
        similarite_ville=0
        
        
        if(len(results)!=0):
            flag=0   ###### nous n'avons pas trouver une ville 
            for row in results:
                    
                codeagence=row[0]
                adresse_a=row[1]
                ville_a=row[2]


                    
                ##### verifier la similariter la ville > 80%
                if(round(jaro_distance(ville_a.lower(),ville.lower()),6)*100 >= 80):
                    
                    if(flag==0):  ##### cas initiale 

                        similarite_adresse=round(jaro_distance(adresse_a,adresse),6)*100
                        similarite_ville=round(jaro_distance(ville_a,ville),6)*100
                        codeagence_Proche=codeagence
                        ville_Proche=ville_a
                        adresse_Proche=adresse_a
                        flag=1  ##### trouver une ville mais pas sur de quartier

                    elif(round(jaro_distance(ville_a.lower(),ville.lower()),6)*100 > similarite_ville):
                        similarite_adresse=round(jaro_distance(adresse_a,adresse),6)*100
                        similarite_ville=round(jaro_distance(ville_a,ville),6)*100
                        codeagence_Proche=codeagence
                        ville_Proche=ville_a
                        adresse_Proche=adresse_a
                        flag=2  ##### trouver une ville plus similaire

                    elif(round(jaro_distance(ville_a.lower(),ville.lower()),6)*100 == similarite_ville): ### cas de même ville
                        if(round(jaro_distance(adresse_a.lower(),adresse.lower()),6)*100 > similarite_adresse and round(jaro_distance(adresse_a.lower(),adresse.lower()),6)*100 >= 80):
                            similarite_adresse=round(jaro_distance(adresse_a,adresse),6)*100
                            similarite_ville=round(jaro_distance(ville_a,ville),6)*100
                            codeagence_Proche=codeagence
                            ville_Proche=ville_a
                            adresse_Proche=adresse_a
                            flag=3  ##### trouver un quartie plus similaire
                    
                        
            db.close()

            if(flag==3):    ###### trouver ville et quartier

                dispatcher.utter_message(text="l'agence la plus proche pour vous c'est&Adresse :"+adresse_Proche+"&Ville :"+ville_Proche+"&Flag :"+str(flag))
                self.flag_agence=True  #### nous avons trouver une agence
                return {"ville":ville,"cherche_agence_1":codeagence_Proche}
            
            elif( (flag==2 or flag==1) and round(jaro_distance(adresse_a.lower(),adresse.lower()),6)*100 < 80):
                ##### cas initiale mais on split l'adresse pour mieux cherche
                flag_2=0
                for row in results:
                    
                    codeagence=row[0]
                    adresse_a=row[1]
                    ville_a=row[2]
                    
                    if(round(jaro_distance(ville_a.lower(),ville.lower()),6)*100 >= 80 and round(jaro_distance(ville_a.lower(),ville.lower()),6)*100 >= similarite_ville): ###### cas ville similaire
                        result=split_adresse_2(adresse_a)
                        similariter_max=max(round(jaro_distance(result[0].lower(),adresse.lower()),6)*100,round(jaro_distance(result[1].lower(),adresse.lower()),6)*100)
                        
                        if( similariter_max > similarite_adresse and similariter_max >= 80):
                            similarite_adresse=similariter_max
                            similarite_ville=round(jaro_distance(ville_a,ville),6)*100
                            codeagence_Proche=codeagence
                            ville_Proche=ville_a
                            adresse_Proche=adresse_a
                            flag_2=1
                
                
                if(flag_2==1):  ### cas nous avons touver une agence selon la ville et le quartier 

                    dispatcher.utter_message(text="l'agence la plus proche pour vous c'est&Adresse :"+adresse_Proche+"&Ville :"+ville_Proche+"&Flag_2 :"+str(flag_2))
                    self.flag_agence=True  #### nous avons trouver une agence

                    return {"ville":ville,"cherche_agence_1":codeagence_Proche}
                
                else:  #### cas nous n'avons pas trouver même avec le splite de l'adresse

                    self.flag_agence=False
                    return {"ville":ville,"cherche_agence_1":ville_Proche}

                

            
            elif(flag==0):  ### cas de même la ville n'existe pas 
                
                self.flag_agence=True
                return {"ville":ville,"cherche_agence_1":False}

                

        else:
            db.close()
            self.flag_agence=True
            return {"ville":ville,"cherche_agence_1":False}

    
    def validate_cherche_agence_2(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker:Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        
        intent=tracker.get_intent_of_latest_message()
        
        
        msg=tracker.latest_message.get("text")
        msg=msg.lower()

        
        if(intent=="chiffre"):
            ville=tracker.get_slot("cherche_agence_1")
            choix=int(msg)
            db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="chatbot_database"
            )

            cursor = db.cursor()

            query1="SELECT agence,adresse,ville,codeagence FROM agences WHERE ville LIKE %s"

            l=[]
            l.append(ville)
            params = (l)

            cursor.execute(query1, params)
            results = cursor.fetchall()
            db.close()
            
            if( len(results)!=0 ):
                if(choix <= len(results) and choix > 0):
                    i=1
                    
                    for row in results:
                        if(choix==i):
                            code_s=row[3]
                            return{"cherche_agence_2":code_s}
                        i=i+1
                else:
                    
                    dispatcher.utter_message(text="le numero saisi est invalide!")
                    return{"cherche_agence_2":None}
        else:
            
            dispatcher.utter_message(response="utter_pardon")          
            return{"cherche_agence_2":None}

    


    def validate_email(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker:Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        
        intent=tracker.get_intent_of_latest_message()
        
        cherche_agence_1=tracker.get_slot("cherche_agence_1")
        msg=tracker.latest_message.get("text")
        msg=msg.lower()
        lis=[]
        lis.append(msg)




        if(verifie_adr_mail(lis)==True):

            if(self.flag_agence==True):
                if(cherche_agence_1 != False):
                    return{'email':msg,'agence_plus_proche':cherche_agence_1}
                else:
                    return{'email':msg,'agence_plus_proche':False}  ### cas meme la ville n'exsite pas
            else: ### nous avons passe aux deuxieme etape
                cherche_agence_2=tracker.get_slot("cherche_agence_2")
                return{'email':msg,'agence_plus_proche':cherche_agence_2}
                
            return{'email':msg,}
        else:
            dispatcher.utter_message(text="l'adresse mail que vous avez saisi est invalide")
            return{'email':None}
        

    def validate_numero_telephone(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker:Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        
        numero_telephone=slot_value
        if verifier_num_tele(numero_telephone) == False:
            dispatcher.utter_message(text="le numero saisi est invalide ")
            return {"numero_telephone":None}
        


        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="chatbot_database"
            )
        
        cursor = db.cursor()
        query1="INSERT INTO demande (typeclient,secteur,codeActivite,cin,resultatTraitement,nom,prenom,adresse,ville,telgsm,email,codeagence) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
      
             ##### enregistrement sur base données #####
            
          
        type_demande=tracker.get_slot('type_demande')
       
        secteur_A=tracker.get_slot('secteur_A')
        activite=tracker.get_slot('activite')
        cin=tracker.get_slot('cin')
        resultatTraitement='Incomplet'
        nom=tracker.get_slot('nom')
        prenom=tracker.get_slot('prenom')
        adresse=tracker.get_slot('adresse')
        ville=tracker.get_slot('ville')
        numero_telephone=tracker.get_slot('numero_telephone')
        
        agence_plus_proche=tracker.get_slot('agence_plus_proche')
        email=tracker.get_slot('email')

        #typeclient,niveauformalisme,secteur,codeActivite,cin,resultatTraitement,nom,prenom,adresse,ville,telgsm,datenaissance,email,codeagence
        values_to_insert = (type_demande,secteur_A,activite,cin,resultatTraitement,nom,prenom,adresse,ville,numero_telephone,email,agence_plus_proche)
        cursor.execute(query1,values_to_insert)

        query2="SELECT LAST_INSERT_ID()"
        cursor.execute(query2)
        results = cursor.fetchall()

        if(len(results)!= 0):
            for row in results:
                self.id_demande=row[0]
        
        global id_demande 
        id_demande = self.id_demande
        db.commit()
        db.close()


        return {"numero_telephone":numero_telephone}
    
    def validate_date_naissance(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker:Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        
        date_naissance=slot_value
        if verifier_date_N(date_naissance,dispatcher) == False:
            dispatcher.utter_message(text="la date saisi est invalide ")
            return {"date_naissance":None}
        elif(verifier_date_N(date_naissance,dispatcher) == "False1"):
            return {"date_naissance":None}

        return {"date_naissance":date_naissance}
    

    def validate_type_numero(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker:Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        
        
        intent=tracker.get_intent_of_latest_message()
        msg=tracker.latest_message.get("text")
        msg=msg.lower()

        if(intent=="patente"):
            return{"type_numero":"patente"}
        elif(intent=="ICE"):
            return{"type_numero":"identifiant commun entreprise"}
        elif(intent=="RC"):
            return{"type_numero":"registre commerce"}
        else:
            L=["patente","identifiant commun entreprise","registre commerce"]
            similariter=0
            typee=""
            for l in L:
                if(round(jaro_distance(msg,l.lower()),6)*100 > 90 and round(jaro_distance(msg,l.lower()),6)*100 > similariter):
                    similariter=round(jaro_distance(msg,l.lower()),6)*100
                    typee=l
            if(typee=="patente"):
                return{"type_numero":"patente"}
            elif(typee=="identifiant commun entreprise"):
                return{"type_numero":"identifiant commun entreprise"}
            elif(typee=="registre commerce"):
                return{"type_numero":"registre commerce"}
            else:
                dispatcher.utter_message(response="utter_pardon")
                return{"type_numero":None}
        

    
    def validate_numero_RC_patente_ICE(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker:Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        
        RC_PT_ICE=slot_value
        intent=tracker.get_intent_of_latest_message()

        if (intent=="chiffre" and verifier_RC_PT_ICE(RC_PT_ICE) == True):
            return {"numero_RC_patente_ICE":RC_PT_ICE}
        
        elif(intent=="chiffre" and verifier_RC_PT_ICE(RC_PT_ICE) == False):
            dispatcher.utter_message(text="le numero saisi est invalide ")
            return {"numero_RC_patente_ICE":None}
        else:
            dispatcher.utter_message(response="utter_pardon")
            return {"numero_RC_patente_ICE":None}
        
    
    def validate_nom_entreprise(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker:Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        
        intent=tracker.get_intent_of_latest_message()
        if(self.EI==True and intent=="inffirmation"): #### cas de EI ce champs et optionnel
            return{"nom_entreprise":False}
        
        name=slot_value
        if len(name) <= 1:
            dispatcher.utter_message(text="le nom d'entreprise saisi est invalide ")
            return {"nom_entreprise":None}
        
        
        return {"nom_entreprise":name}
    
    def validate_GSME(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker:Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        
        numero_telephone=slot_value
        intent=tracker.get_intent_of_latest_message()
        if(self.EI==True and intent=="inffirmation"):
            return{"GSME":False}

        if(intent=="chiffre" and  verifier_num_tele(numero_telephone) == True):
            return {"GSME":numero_telephone}
        elif(intent=="chiffre" and  verifier_num_tele(numero_telephone) == False):
            dispatcher.utter_message(text="le numero saisi est invalide ")
            return {"GSME":None}
        else:
            dispatcher.utter_message(response="utter_pardon")
            return {"GSME":None}

    def validate_adresse_entreprise(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker:Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        
        adresse=slot_value
        intent=tracker.get_intent_of_latest_message()
        if(self.EI==True and intent=="inffirmation"):
            return{"adresse_entreprise":False}
        if len(adresse) <= 4:
            dispatcher.utter_message(text="l'adresse saisi est invalide")
            return {"adresse_entreprise":None}
        return {"adresse_entreprise":adresse}
    
    def validate_ville_entreprise(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker:Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        
        ville=slot_value
        intent=tracker.get_intent_of_latest_message()
        if(self.EI==True and intent=="inffirmation"):
            return{"ville_entreprise":False}
        if len(ville) <= 2:
            dispatcher.utter_message(text="la ville saisie est invalide")
            return {"ville_entreprise":None}
        return {"ville_entreprise":ville}
    
    def validate_frome_juridique(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker:Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        
       
        msg=tracker.latest_message.get("text")
        msg=msg.lower()
        intent=tracker.get_intent_of_latest_message()

        if((intent=="chiffre" and msg=="1")):
            return{'frome_juridique':'C'}
        elif((intent=="chiffre" and msg=="2")):
            return{'frome_juridique':'D'}
        elif((intent=="chiffre" and msg=="3")):
            return{'frome_juridique':'E'}
        elif((intent=="chiffre" and msg=="4")):
            return{'frome_juridique':'F'}
        elif((intent=="chiffre" and msg=="5")):
            return{'frome_juridique':'G'}
        elif((intent=="chiffre" and msg=="6")):
            return{'frome_juridique':'H'}
        elif((intent=="chiffre" and msg=="7")):
            return{'frome_juridique':"I"}
        elif((intent=="chiffre" and msg=="8")):
            return{'frome_juridique':'J'}
        elif((intent=="chiffre" and msg=="9")):
            return{'frome_juridique':'K'}
        elif((intent=="chiffre" and msg=="10")):
            return{'frome_juridique':'M'}
        elif((intent=="chiffre" and msg=="11")):
            return{'frome_juridique':'B'}
        elif(intent=="forme_juridique"):
            L=["Societe en nom collectif","Societe en commandite simple","Association ou ste en participation","Societe anonyme","Societe en commandite par action","Societe a responsabilte limitee","S.A.R.L. d'associe unique","Societe cooperative","Societe civile","Societe de fait","Entrepreneur individuel"]
            similariter=0
            index=100
            i=1
            for l in L:
                if(round(jaro_distance(msg,l.lower()),6)*100 > 90 and round(jaro_distance(msg,l.lower()),6)*100 > similariter):
                    similariter=round(jaro_distance(msg,l.lower()),6)*100
                    index=i
                i=i+1
            if(index==1):
                return{'frome_juridique':'C'}
            elif(index==2):
                return{'frome_juridique':'D'}
            elif(index==3):
                return{'frome_juridique':'E'}
            elif(index==4):
                return{'frome_juridique':'F'}
            elif(index==5):
                return{'frome_juridique':'G'}
            elif(index==6):
                return{'frome_juridique':'H'}
            elif(index==7):
                return{'frome_juridique':"I"}
            elif(index==8):
                return{'frome_juridique':'J'}
            elif(index==9):
                return{'frome_juridique':'K'}
            elif(index==10):
                return{'frome_juridique':'M'}
            elif(index==11):
                return{'frome_juridique':'B'}
            
        elif((intent=="inffirmation")):
            dispatcher.utter_message(response="utter_malheuressement")
            return{'frome_juridique':False}
        else:
            dispatcher.utter_message(response="utter_pardon")
            return{'frome_juridique':None}

    
    
    def validate_offre(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker:Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        
        
        msg=tracker.latest_message.get("text")
        msg=msg.lower()
        intent=tracker.get_intent_of_latest_message()
        offre=tracker.get_slot('offre')
        #tracker.get_latest_entity_values("offre_souhaitez")
        if(intent=="question_concernant_offre"):
            ent = tracker.latest_message['entities'][0]['value']
        else:
            ent=""
        
        ent=ent.lower()
        if (((intent == "chiffre" and msg=="1") or (intent=="question_concernant_offre" and ent=="tanmiya")) and self.PP == False):
            return{'offre':'tanmiya'}
        elif (((intent == "chiffre" and msg=="2") or(intent=="question_concernant_offre" and ent=="moumtaz")) and self.PP == False):
            return{'offre':'moumtaz'}
        elif (((intent == "chiffre" and msg=="3") or (intent=="question_concernant_offre" and ent=="milkia")) and self.PP == False):
            return{'offre':'milkia'}
        elif (((intent == "chiffre" and msg=="4") or (intent=="question_concernant_offre" and ent=="milkia")) and self.PP == False):
            return{'offre':'milkia'}
        elif (((intent == "chiffre" and msg=="5") or (intent=="question_concernant_offre" and ent=="oto")) and self.PP == False):
            return{'offre':'oto'}
        elif (((intent == "chiffre" and msg=="1") or (intent=="question_concernant_offre" and ent=="pie")) and self.PP == True):
            return{'offre':'pie'}
        elif (((intent == "chiffre" and msg=="2") or (intent=="question_concernant_offre" and ent=="pil")) and self.PP == True):
            return{'offre':'pil'}
        else:
            dispatcher.utter_message(response="utter_pardon")
            return{'offre':None}
        
    def validate_montant_souhaite(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker:Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        
        
        msg=tracker.latest_message.get("text")
        msg=msg.lower()
        
        intent=tracker.get_intent_of_latest_message()
        offre=tracker.get_slot('offre')
        
        if(intent=='montant' or intent=="chiffre"):
            msg=clean_montant(msg)
            if((offre=="tanmiya" or offre=="moumtaz") and float(msg) >= 50000.0 and float(msg) <= 150000.0):
                return{'montant_souhaite':msg}
            elif((offre=="oto" or offre=="milkia") and float(msg) >= 10000.0 and float(msg) <= 150000.0):
                return{'montant_souhaite':msg}
            elif((offre=="pil" or offre=="pie") and float(msg) >= 1000.0 and float(msg) <= 48000.0):
                return{'montant_souhaite':msg}
            else:
                dispatcher.utter_message(text="le montant que vous avez entré n'est pas valide pour l'offre choisi")
                return{'montant_souhaite':None}
        else:
            dispatcher.utter_message(text="merci de saisir le montant en chiffre")
            return{'montant_souhaite':None}
        
    def validate_type_locale(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker:Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        
        
        msg=tracker.latest_message.get("text")
        msg=msg.lower()
        intent=tracker.get_intent_of_latest_message()
        offre=tracker.get_slot('offre')
        global flag_type_local
        if((intent=="chiffre" and msg=="1") or intent=="locataire" ):
            return{'type_locale':'locataire'}
        elif((intent=="chiffre" and msg=="2") or intent=="proprietaire"):
            return{'type_locale':'proprietaire'}
        elif(intent=="inffirmation"):
            if((offre == 'tanmiya' or offre == 'moumtaz' or offre == 'milkia' or offre=='oto') and flag_type_local==0):
                flag_type_local=1
                return{'type_locale':None}
            else:
                dispatcher.utter_message(response="utter_malheuressement")
                return{'type_locale':False}
        else:
            dispatcher.utter_message(response="utter_pardon")
            return{'type_locale':None}
        
    def validate_garantie(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker:Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        
        
        msg=tracker.latest_message.get("text")
        msg=msg.lower()
        intent=tracker.get_intent_of_latest_message()
        offre=tracker.get_slot('offre')
        global flag_type_local
        type_locale=tracker.get_slot('type_locale')
        if((offre=="tanmiya" or offre=="moumtaz" or offre=="oto" or offre=="milkia") and flag_type_local==0):
            if((intent=="chiffre" and msg=="1") or intent=="garantie_1"):
                return{'garantie':'Fond de commerce '}
            elif((intent=="chiffre" and msg=="2") or intent=='garantie_2'):
                return{'garantie':"contrat d'hypotheque"}
            elif(intent=="inffirmation"):
                dispatcher.utter_message(response="utter_malheuressement")
                return{'garantie':False}
            else:
                dispatcher.utter_message(response="utter_pardon")
                return{'garantie':None}
            
        elif(offre=="pil" or offre=="pie" or flag_type_local==1):
            if(type_locale=="locataire"):
                if((intent=="chiffre" and msg=="1") or intent=="garantie_1_L"):
                    return{'garantie':'reconnaissance de dette'}
                elif((intent=="chiffre" and msg=="2")or intent=="garantie_2_L"):
                    return{'garantie':'nantissement des biens'}
                elif((intent=="chiffre" and msg=="3") or intent=="garantie_3_L"):
                    return{'garantie':"caution d'un tiers"}
                elif(intent=="inffirmation"):
                    dispatcher.utter_message(response="utter_malheuressement")
                    return{'garantie':False}
                else:
                    dispatcher.utter_message(response="utter_pardon")
                    return{'garantie':None}
            elif(type_locale=="proprietaire"):
                if((intent=="chiffre" and msg=="1") or intent=="garantie_2"):
                    return{'garantie':"contrat d'hypotheque"}
                elif((intent=="chiffre" and msg=="2")or intent=="garantie_3_L"):
                    return{'garantie':"caution d'un tiers"}
                elif(intent=="inffirmation"):
                    dispatcher.utter_message(response="utter_malheuressement")
                    return{'garantie':False}    
                else:
                    dispatcher.utter_message(response="utter_pardon")
                    return{'garantie':None}
           

    def validate_revenu_mensuel(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker:Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        
        msg=tracker.latest_message.get("text")
        msg=msg.lower()
        
        intent=tracker.get_intent_of_latest_message()
        offre=tracker.get_slot('offre')
        if(intent=='montant' or intent=="chiffre"):
            msg=clean_montant(msg)
            if(float(msg)<500):
                dispatcher.utter_message(text="le montant saisi est invalide!")
                return {'revenu_mensuel':None}
            return{'revenu_mensuel':msg}
        else:
            dispatcher.utter_message(text="merci de saisir le montant en chiffre")
            return{'revenu_mensuel':None}
    
    def validate_charges_mensuelles(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker:Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        
        msg=tracker.latest_message.get("text")
        msg=msg.lower()
        
        intent=tracker.get_intent_of_latest_message()
        offre=tracker.get_slot('offre')
        if(intent=='montant' or intent=="chiffre"):
            msg=clean_montant(msg)
            return{'charges_mensuelles':msg}
        else:
            dispatcher.utter_message(text="merci de saisir le montant en chiffre")
            return{'charges_mensuelles':None}

    def validate_charges_familiales(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker:Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        
        msg=tracker.latest_message.get("text")
        msg=msg.lower()
        
        intent=tracker.get_intent_of_latest_message()
        offre=tracker.get_slot('offre')
        if(intent=='montant' or intent=="chiffre"):
            msg=clean_montant(msg)
            return{'charges_familiales':msg}
        else:
            dispatcher.utter_message(text="merci de saisir le montant en chiffre")
            return{'charges_familiales':None}
    
    
    def validate_excedant(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker:Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        
        msg=tracker.latest_message.get("text")
        msg=msg.lower()
        
        intent=tracker.get_intent_of_latest_message()
        offre=tracker.get_slot('offre')
        revenu=float(tracker.get_slot('revenu_mensuel'))
        charge_M=float(tracker.get_slot('charges_mensuelles'))
        charge_F=float(tracker.get_slot('charges_familiales'))
        montant_souhaite=tracker.get_slot('montant_souhaite')

        self.ex_cal=revenu-charge_F-charge_M

        if(intent=='montant' or intent=="chiffre"):
            msg=clean_montant(msg)
            self.etat=valide_excedant(float(msg),revenu,charge_M,charge_F,0.1)
            if(self.etat==3):
                if(Evaluation_patrimoine(offre,float(montant_souhaite),self.ex_cal)==True):
                    dispatcher.utter_message(text="Très bien, vous êtes éligible pour le montant que vous avez demandé")
                else:
                    mont=Evaluation_patrimoine(offre,float(montant_souhaite),self.ex_cal)
                    dispatcher.utter_message(text="Malheureusement, vous ne pouvez pas obtenir le montant demandé &selon votre situation financière vous pourriez avoir un montant "+ str(mont) +"DH")
                
            return{'excedant':msg}
        elif(intent=='inffirmation'):
            dispatcher.utter_message(response="utter_malheuressement")
            self.etat=-1
            return{'excedant':False}
        else:
            dispatcher.utter_message(text="merci de saisir le montant en chiffre")
            return{'excedant':None}
        
    def validate_autre_revenu(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker:Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        
        msg=tracker.latest_message.get("text")
        msg=msg.lower()
        
        intent=tracker.get_intent_of_latest_message()
        offre=tracker.get_slot('offre')
        
        montant_souhaite=tracker.get_slot('montant_souhaite')
        if(intent=='montant' or intent=="chiffre"):
            msg=clean_montant(msg)
            self.ex_cal=self.ex_cal+float(msg)  #### update de excédant calculer
            
            if(Evaluation_patrimoine(offre,float(montant_souhaite),self.ex_cal)==True):
                dispatcher.utter_message(text="Très bien, vous êtes éligible pour le montant que vous avez demandé")
                return{'autre_revenu':msg}
            else:
                mont=Evaluation_patrimoine(offre,float(montant_souhaite),self.ex_cal)
                dispatcher.utter_message(text="Malheureusement, vous ne pouvez pas obtenir le montant demandé &selon votre situation financière vous pourriez avoir un montant "+ str(mont) +"DH")
                return{'autre_revenu':msg}

        elif(intent=='inffirmation'):
            if(Evaluation_patrimoine(offre,float(montant_souhaite),self.ex_cal)==True):
                dispatcher.utter_message(text="Très bien, vous êtes éligible pour le montant que vous avez demandé")
                return{'autre_revenu':'0'}
            else:
                mont=Evaluation_patrimoine(offre,float(montant_souhaite),self.ex_cal)
                dispatcher.utter_message(text="Malheureusement, vous ne pouvez pas obtenir le montant demandé &selon votre situation financière vous pourriez avoir un montant "+ str(mont)+"DH")
                return{'autre_revenu':'0'}
            
        else:
            dispatcher.utter_message(text="merci de saisir le montant en chiffre")
            return{'autre_revenu':None}
        
    def validate_autres_pret(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker:Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        
        msg=tracker.latest_message.get("text")
        msg=msg.lower()
        
        intent=tracker.get_intent_of_latest_message()
        offre=tracker.get_slot('offre')
        montant_souhaite=tracker.get_slot('montant_souhaite')

        if(intent=='montant' or intent=="chiffre"):
            msg=clean_montant(msg)
            self.ex_cal=self.ex_cal-float(msg)  #### update de excédant calculer
            
            if(Evaluation_patrimoine(offre,float(montant_souhaite),self.ex_cal)==True):
                
                dispatcher.utter_message(text="Très bien, vous êtes éligible pour le montant que vous avez demandé")
                return{'autres_pret':msg}
            else:
                
                mont=Evaluation_patrimoine(offre,float(montant_souhaite),self.ex_cal)
                dispatcher.utter_message(text="Malheureusement, vous ne pouvez pas obtenir le montant demandé &selon votre situation financière vous pourriez avoir un montant "+ str(mont)+"DH")
                return{'autres_pret':msg}
            
        elif(intent=='inffirmation'):
            if(Evaluation_patrimoine(offre,float(montant_souhaite),self.ex_cal)==True):
                
                dispatcher.utter_message(text="Très bien, vous êtes éligible pour le montant que vous avez demandé")
                return{'autres_pret':'0'}
            else:
                
                mont=Evaluation_patrimoine(offre,float(montant_souhaite),self.ex_cal)
                dispatcher.utter_message(text="Malheureusement, vous ne pouvez pas obtenir le montant demandé &selon votre situation financière vous pourriez avoir un montant "+ str(mont)+"DH")
                return{'autres_pret':'0'}
        else:
            dispatcher.utter_message(text="merci de saisir le montant en chiffre")
            return{'autres_pret':None}
        
    def validate_confirmer_demande(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker:Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        
        msg=tracker.latest_message.get("text")
        msg=msg.lower()
        
        intent=tracker.get_intent_of_latest_message()
        offre=tracker.get_slot('offre')
        montant_souhaite=tracker.get_slot('montant_souhaite')
        montant=Evaluation_patrimoine(offre,float(montant_souhaite),self.ex_cal)

        if(Evaluation_patrimoine(offre,float(montant_souhaite),self.ex_cal)==True):
                montant=float(montant_souhaite)
        
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="chatbot_database"
            )
        
        cursor = db.cursor()        
        query="UPDATE demande SET ice=%s,typeLocal=%s,rcommerce=%s,resultatTraitement=%s,raisonsociale=%s,numpattente=%s,formejuridique=%s,adresseentreprise=%s,villeentreprise=%s,montantdemande=%s,produit=%s,revenu_mensuel=%s,charges_mensuelles=%s,charges_familiales=%s,autre_pret=%s,autre_revenu=%s,excedant=%s,type_garantie=%s,montant_possible=%s,datenaissance=%s WHERE id=%s"
        
        
        
        type_demande=tracker.get_slot("type_demande")           
        typeLocal=False   #### a regler
        date_naissance=tracker.get_slot("date_naissance")
        revenu_mensuel=tracker.get_slot('revenu_mensuel')
        charges_mensuelles=tracker.get_slot('charges_mensuelles')
        charges_familiales=tracker.get_slot('charges_familiales')
        excedant=tracker.get_slot('excedant')
          
        type_locale=tracker.get_slot('type_locale')            
        garantie=tracker.get_slot('garantie')
                    

        if(self.etat==1):
            autre_revenu=tracker.get_slot('autre_revenu')
            autres_pret=False

        if(self.etat==2):
            autres_pret=tracker.get_slot('autres_pret')
            autre_revenu=False

        if(self.etat==3):
            autre_revenu=False
            autres_pret=False

        if(type_demande=="PM" or type_demande=="EI"):
                
            nom_entreprise=tracker.get_slot('nom_entreprise')
            gsme=tracker.get_slot('GSME')

            type_numero=tracker.get_slot('type_numero')
            numero=tracker.get_slot("numero_RC_patente_ICE")

            if(type_numero=="patente"):
                patent=numero
                ice=False
                rc=False
            elif(type_numero=="identifiant commun entreprise"):
                patent=False
                ice=numero
                rc=False
            elif(type_numero=="registre commerce"):
                patent=False
                ice=False
                rc=numero
            adresse_entreprise=tracker.get_slot('adresse_entreprise')
            ville_entreprise=tracker.get_slot('ville_entreprise')
            frome_juridique=tracker.get_slot('frome_juridique')

            
                
        if(type_demande=="PP"):
                
                
            patent=False
            ice=False
            rc=False
            nom_entreprise=False
            gsme=False
            adresse_entreprise=False
            frome_juridique=False
            ville_entreprise=False

            

        
        ##### cas de confirmation 

        if((intent=="chiffre" and msg=="1") or intent=="affirmation"):

            dispatcher.utter_message(text="Votre demande a été prise en considération, merci de nous avoir choisi &Un conseiller prendra attache avec vous incessamment pour finaliser la suite du processus.")

            resultatTraitement='Intéressé'

            values_to_insert = (ice,type_locale,rc,resultatTraitement,nom_entreprise,patent,frome_juridique,adresse_entreprise,ville_entreprise,montant_souhaite,offre,revenu_mensuel,charges_mensuelles,charges_familiales,autres_pret,autre_revenu,excedant,garantie,montant,date_naissance,self.id_demande)
            cursor.execute(query,values_to_insert)



            db.commit()
            db.close()

            return{'confirmer_demande':True,'montant_finale':montant}
        

        ###### pas de confirmation

        elif((intent=="chiffre" and msg=="2") or intent=="inffirmation"):
            
            if(Evaluation_patrimoine(offre,float(montant_souhaite),self.ex_cal)==True):
                montant=float(montant_souhaite)
            else:
                montant=Evaluation_patrimoine(offre,float(montant_souhaite),self.ex_cal)
                
            dispatcher.utter_message(text="D'accord pas de problème& si vous changez votre avis nous sommes toujours à votre disposition")
                       
            resultatTraitement='PasIntéressé'
           
            values_to_insert = (ice,type_locale,rc,resultatTraitement,nom_entreprise,patent,frome_juridique,adresse_entreprise,ville_entreprise,montant_souhaite,offre,revenu_mensuel,charges_mensuelles,charges_familiales,autres_pret,autre_revenu,excedant,garantie,montant,date_naissance,self.id_demande)
            cursor.execute(query,values_to_insert)
            db.commit()
            db.close()
            return{'confirmer_demande':False,'montant_finale':montant}
        
        else:

            dispatcher.utter_message(response="utter_pardon")
            db.close()
            return{'confirmer_demande':None,'montant_finale':None}



class Action_Q_A_G_revenu(Action):

     def name(self) -> Text:
         return "action_ask_A_G_revenu"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         dispatcher.utter_message(response="utter_Q_A_G_revenu")
         return []

class Action_Q_6mois(Action):

     def name(self) -> Text:
         return "action_ask_six_mois_activite"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         dispatcher.utter_message(response="utter_Q_6mois")
         return []

class Action_Q_condition(Action):

     def name(self) -> Text:
         return "action_ask_condition"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         dispatcher.utter_message(response="utter_Q_condition")
         return []


     

class Action_Q_offre(Action):

     def name(self) -> Text:
         return "action_ask_offre"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         type_demande=tracker.get_slot("type_demande")
         if(  type_demande == 'PM' or type_demande == 'EI'):
             dispatcher.utter_message(response="utter_Q_offre_PM_EI")
         elif(type_demande == 'PP'):
             dispatcher.utter_message(response="utter_Q_offre_PP")

         return []

class Action_Q_agence_proche(Action):

     def name(self) -> Text:
         return "action_ask_cherche_agence_2"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         
         ville=tracker.get_slot("cherche_agence_1")

         db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="chatbot_database"
            )

         cursor = db.cursor()

         query1="SELECT agence,adresse,ville,codeagence FROM agences WHERE ville LIKE %s"

         l=[]
         l.append(ville)
         params = (l)

         cursor.execute(query1, params)
         results = cursor.fetchall()
         i=1
         if(len(results)!=0):
            
            dispatcher.utter_message(text="Voici la liste des agences situées dans votre ville. Veuillez choisir celle qui est la plus proche de vous en saisissant son numéro.")
            for row in results:
                    
                    agence_s=row[0]
                    adresse_s=row[1]
                    ville_s=row[2]
                    dispatcher.utter_message(text=""+str(i)+" # adresse: "+adresse_s+"&agence: "+agence_s+"&ville: "+ville_s)
                    i=i+1
         return []

class Action_Q_montant_souhaite(Action):

     def name(self) -> Text:
         return "action_ask_montant_souhaite"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         type_offre=tracker.get_slot("offre")
         type_offre=type_offre.lower()
         
         if(  type_offre == 'tanmiya' or type_offre == 'moumtaz'):
             dispatcher.utter_message(response="utter_Q_montant_1")
         elif(type_offre == 'milkia' or type_offre=='oto'):
             dispatcher.utter_message(response="utter_Q_montant_2")
         elif(type_offre == 'pie' or type_offre=='pil'):
             dispatcher.utter_message(response="utter_Q_montant_3")
        

         return []

class Action_Q_type_locale(Action):

     def name(self) -> Text:
         return "action_ask_type_locale"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         type_offre=tracker.get_slot("offre")
         type_offre=type_offre.lower()
         global flag_type_local
         if((type_offre == 'tanmiya' or type_offre == 'moumtaz' or type_offre == 'milkia' or type_offre=='oto') and flag_type_local==0):
             dispatcher.utter_message(response="utter_Q_type_locale_2")
         
         elif(type_offre == 'pie' or type_offre=='pil' or flag_type_local==1):
             dispatcher.utter_message(response="utter_Q_type_locale_1")
        

         return []

class Action_Q_garantie(Action):

     def name(self) -> Text:
         return "action_ask_garantie"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         type_offre=tracker.get_slot("offre")
         type_locale=tracker.get_slot("type_locale")
         global flag_type_local
         if((type_offre == 'tanmiya' or type_offre == 'moumtaz' or type_offre == 'milkia' or type_offre=='oto') and flag_type_local== 0 ):
             dispatcher.utter_message(text="Est-ce que vous disposez de l'une des garanties suivantes ?&&1 # Nantissement de Fond de commerce&2 # Contrat d'hypothèque")
         
         elif(type_offre == 'pie' or type_offre=='pil' or flag_type_local== 1):
             if(type_locale=="proprietaire"):
                dispatcher.utter_message(text= "Est-ce que vous disposez de l'une des garanties suivantes ? &&1 # Contrat d'hypothèque&2 # Est-ce que vous avez quelqu'un qui peut vous garantir ")
             else:
                 dispatcher.utter_message(text="est-ce que vous disposez de l'une des garanties suivantes ?&&1 # Reconnaissance de dette&2 # Contrat de nantissement des biens&3 # Est-ce que vous avez quelqu'un qui peut vous garantir")

                
        

         return []

class Action_fall_back(Action):

     def name(self) -> Text:
         return "action_fallback"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         
         msg=tracker.latest_message.get("text")
         msg=msg.lower()


         db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="chatbot_database"
            )
        
         cursor = db.cursor()        
         query="INSERT INTO message_a_repondre (message) VALUES (%s)"
         L=[]
         L.append(msg)
         values_to_insert = (L)
         cursor.execute(query,values_to_insert)
         db.commit()
         db.close()


         dispatcher.utter_message(text="Je suis désolé, mais je ne suis pas en mesure de répondre à votre demande pour le moment. Je vais transmettre votre message à notre équipe d'assistance et nous reviendrons vers vous dès que possible.&Merci de votre compréhension et de votre patience !")
         
         return [UserUtteranceReverted()]

class Action_stop_form1(Action):
    def name(self) -> Text:
        return "action_stop_form1"
    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        


        
        numero_telephone=tracker.get_slot('numero_telephone')
        last_requested_slot = tracker.get_slot("requested_slot")
        
    
        if(numero_telephone != None):

            db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="chatbot_database"
            )

            cursor = db.cursor()
           # query1="INSERT INTO demande_non_complet (a_g_revenu,six_mois_activite,type_demande,justification,contrat,secteur_activite,activite,nom,prenom,cin,adresse,ville,agence_plus_proche,email,numero_telephone,date_naissance,numero_RC_patente_ICE,nom_entreprise,gsm_entreprise,adresse_entreprise,frome_juridique,offre,montant_souhaite,garantie,revenu_mensuel,charges_mensuelles,charges_familiales,excedant,autre_revenu,autres_pret,montant_finale) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            query="UPDATE demande SET ice=%s,typeLocal=%s,rcommerce=%s,resultatTraitement=%s,raisonsociale=%s,numpattente=%s,formejuridique=%s,adresseentreprise=%s,villeentreprise=%s,montantdemande=%s,produit=%s,revenu_mensuel=%s,charges_mensuelles=%s,charges_familiales=%s,autre_pret=%s,autre_revenu=%s,excedant=%s,type_garantie=%s,montant_possible=%s,datenaissance=%s WHERE id = %s"

            type_demande=tracker.get_slot('type_demande')
            montant=0
            date_naissance=0
            typelocal=0
            nom_entreprise=0
            gsme=0
            adresse_entreprise=0
            ville_entreprise=0
            frome_juridique=0
            offre=0
            montant_souhaite=0
            garantie=0
            revenu_mensuel=0
            charges_mensuelles=0
            charges_familiales=0
            excedant=0
            autre_revenu=0
            autres_pret=0
            patent=0
            rc=0
            ice=0
            resultatTraitement="Incomplet"


            slot_list=["date_naissance","numero_RC_patente_ICE",'nom_entreprise','GSME','adresse_entreprise','ville_entreprise','frome_juridique','offre','montant_souhaite','type_locale',"garantie","revenu_mensuel",'charges_mensuelles','charges_familiales','excedant','autre_revenu','autres_pret']
            
            

            #######################################################################################################################
            
            etat=6
            for slot in slot_list:
                if(last_requested_slot==slot):
                    
                    break
                
                elif(slot=="date_naissance" ):
                    date_naissance=tracker.get_slot("date_naissance")
                
                    continue
                elif(slot=="numero_RC_patente_ICE" and (type_demande=="EI" or type_demande=="PM")):
                    type_numero=tracker.get_slot("type_numero")
                    numero=tracker.get_slot("numero_RC_patente_ICE")
                    if(type_numero=="patente"):
                        patent=numero
                        ice=False
                        rc=False
                    elif(type_numero=="identifiant commun entreprise"):
                        patent=False
                        ice=numero
                        rc=False
                    elif(type_numero=="registre commerce"):
                        patent=False
                        ice=False
                        rc=numero
                   
                    continue
                elif(slot=="nom_entreprise" and (type_demande=="EI" or type_demande=="PM")):
                    nom_entreprise=tracker.get_slot("nom_entreprise")
                 
                    continue

                elif(slot=="GSME" and (type_demande=="EI" or type_demande=="PM")):
                    gsme=tracker.get_slot("GSME")
                  
                    continue

                elif(slot=="adresse_entreprise" and (type_demande=="EI" or type_demande=="PM")):
                    adresse_entreprise=tracker.get_slot("adresse_entreprise")
                   
                    continue

                elif(slot=="ville_entreprise" and (type_demande=="EI" or type_demande=="PM")):
                    ville_entreprise=tracker.get_slot("ville_entreprise")
                   
                    continue

                elif(slot=="frome_juridique" and (type_demande=="EI" or type_demande=="PM")):
                    frome_juridique=tracker.get_slot("frome_juridique")
                    
                    continue

                elif(slot=="offre"):
                    offre=tracker.get_slot("offre")
                 
                    continue

                elif(slot=="montant_souhaite"):
                    montant_souhaite=tracker.get_slot("montant_souhaite")
                 
                    continue
                elif(slot=="type_locale"):
                    typelocal=tracker.get_slot("type_locale")

                elif(slot=="garantie"):
                    garantie=tracker.get_slot("garantie")
                    if((type_demande=="EI" or type_demande=="PM") and garantie=="1"):
                        garantie="titre foncier du bien"
                        
                        continue
                    elif((type_demande=="EI" or type_demande=="PM") and garantie=="2"):
                        garantie="garant"
                       
                        continue
                    elif((type_demande=="PP") and garantie=="1"):
                        garantie="Reconnaissance de dette"
                       
                        continue
                    elif((type_demande=="PP") and garantie=="2"):
                        garantie="Contrat de nantissement des biens"
                        
                        continue
                    elif((type_demande=="PP") and garantie=="3"):
                        garantie="Contrat d'hypothèque"
                        
                        continue

                elif((slot=="revenu_mensuel")):
                    revenu_mensuel=tracker.get_slot("revenu_mensuel")
                   
                    continue
                elif((slot=="charges_mensuelles")):
                    charges_mensuelles=tracker.get_slot("charges_mensuelles")
                    
                    continue
                elif((slot=="charges_familiales")):
                    charges_familiales=tracker.get_slot("charges_familiales")
                  
                    continue
                elif(slot=="excedant"):
                    excedant=tracker.get_slot("excedant")
                   
                    continue
                elif(slot=="autre_revenu" and etat==1):
                    autre_revenu=tracker.get_slot("autre_revenu")
                    
                    continue
                elif(slot=="autres_pret"and etat==2):
                    autres_pret=tracker.get_slot("autres_pret")
                    
                    continue

                
            
                
            global id_demande
            
            #ice=%s,rcommerce=%s,resultatTraitement=%s,raisonsociale=%s,numpattente=%s,formejuridique=%s,adresseentreprise=%s,villeentreprise=%s,montantdemande=%s,produit=%s,revenu_mensuel=%s,charges_mensuelles=%s,charges_familiales=%s,autre_pret=%s,autre_revenu=%s,excedant=%s,type_garantie=%s,montant_possible=%s,datenaissance=%s id=%s"
            values_to_insert = (ice,typelocal,rc,resultatTraitement,nom_entreprise,patent,frome_juridique,adresse_entreprise,ville_entreprise,montant_souhaite,offre,revenu_mensuel,charges_mensuelles,charges_familiales,autres_pret,autre_revenu,excedant,garantie,montant,date_naissance,id_demande)
            cursor.execute(query,values_to_insert)
            db.commit()
            db.close()
            
            
        dispatcher.utter_message(response="utter_stop_reponse")



def verifier_cin(cin):
    alp=['a','b','c','d','e','f','j','h','i','g','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    num=['1','2','3','4','5','6','7','8','9','0']
    if(len(cin) < 6 or len(cin) > 8):
        return False
    else:
        if(cin[0].lower() in alp and cin[1].lower() not in alp):
            for i in cin[1:]:
                if(i not in num):
                    return False
                
            return True
            
        elif((cin[0].lower() in alp) and (cin[1].lower() in alp)):
             for i in cin[2:]:
                if(i not in num):
                    return False
         
             return True
        
        else:
            return False

def verifier_num_tele(tele):
    
    num=['1','2','3','4','5','6','7','8','9','0']
    if((len(tele) == 10 and tele[0] == '0' and tele[1] == '6')or(len(tele) == 10 and tele[0] == '0' and tele[1] == '7')or(len(tele) == 10 and tele[0] == '0' and tele[1] == '5')or(len(tele) == 10 and tele[0] == '0' and tele[1] == '8')):
        for x in tele:
            if(x not in num): 
                return False
        return True
    else:
        return False
    
def verifier_date_N(DN,dispatcher: CollectingDispatcher):
    
    num=['1','2','3','4','5','6','7','8','9','0']
    i=0
    today = datetime.date.today()
    year = today.strftime("%Y")

    if(DN[2]=='-' and DN[5]=='-' and len(DN) == 10):
        while(i<10):
            if(i != 2 and i != 5 and DN[i] not in num):
                return False
            i=i+1
        jj=int(DN[0]+DN[1])
        mm=int(DN[3]+DN[4])
        aa=int(DN[6]+DN[7]+DN[8]+DN[9])
        if(jj <= 0 or jj>31):
            return False
        elif(mm <= 0 or mm > 12):
            return False
        elif( aa < int(year)-100 or aa > int(year)):
            return False
        elif(int(year)-aa) <= 17:
            dispatcher.utter_message(text="Selon la date que vous avez saisie, vous n'avez pas l'âge légal pour disposer d'une demande de prêt")
            return "False1"
        else:
            return True
    else:
        return False

def verifier_RC_PT_ICE(numm):
    num=['1','2','3','4','5','6','7','8','9','0']
    if(len(numm)<=15 and len(numm) >=9):
        for x in numm:
            if(x not in num): 
                return False
        return True
    else:
        return False
    
def verifier_montant(montant):
    num=['1','2','3','4','5','6','7','8','9','0','d','h','s']
    cntnum=0
    cntlettre=''
    for x in montant:
        if(x not in num): 
            cntlettre=cntlettre+x
        cntnum=+1
    if(cntnum<4):
        return False
    
    
def clean_montant(name):
    num=['1','2','3','4','5','6','7','8','9','0']
    res=""
    flag=False
    cc=0
    for x in name:
        if(x in num and flag==False):
            res=res+x
        if(x in num and flag==True and cc<2):
            res=res+x
            cc=cc+1
        if((x=='.' or x==',') and flag==False):
            res=res+'.'
            flag=True
    return res

def valide_excedant(ex_dec,revenu,charges_M,charges_F,pourcentage):

    ex_cal=revenu-charges_F-charges_M

    varience=ex_cal*pourcentage

    if (ex_cal+varience < ex_dec ):
        return 1  #### excedant declarer plus grand de excedant calculer de 10%
    elif(ex_cal-varience > ex_dec):
        return 2  #### excedant declarer mois de excedant calculer
    elif((ex_cal <= ex_dec and ex_dec <= ex_cal+varience)or(ex_cal >= ex_dec and ex_cal-varience <= ex_dec )):
        return 3  #### excedant compatible
    else:
        return 0
    
def verifie_adr_mail(L):
    """vérifie la syntaxe d'une liste d'adresses mail données sous forme de chaine"""
    R = [] # future liste des adresses valides
    E = [] # future liste des adresses invalides
    reExt = re.compile(r"^[^<>]*<([^<>]+)>$|(^[^<>]+$)")
    reVerif = re.compile(r"^[a-zA-Z0-9_\-]+(\.[a-zA-Z0-9_\-]+)*@[a-zA-Z0-9_\-]+(\.[a-zA-Z0-9_\-]+)*(\.[a-zA-Z]{2,6})$")
    for ch in L:
        # extraction de l'adresse même dans le cas 'yyyyy <xxxx@xxxx.xxx>' 
        a = reExt.findall(ch.strip())
        if len(a)>0:
            adr = ''.join(a[0]).strip()
        else:
            adr = ''
        # vérification de syntaxe de l'adresse mail extraite
        if adr=='':
            #E.append(ch)
            return False
        else:
            if reVerif.match(adr)!=None:
                #R.append(ch)
                return True
            else:
                #E.append(ch)
                return False

def Evaluation_patrimoine(offre,montant_souhaite,excedant):
    
    capaciter_client=excedant*0.45
    echience=round(montant_souhaite/capaciter_client)
    

    
    if(offre=="moumtaz"):
        if(echience <= 60):
            return True
        else:
            return capaciter_client*60   ### montant proposer
    elif(offre=="milkia"):
        if(echience <= 60):
            return True
        else:
            return capaciter_client*60   ### montant proposer
    elif(offre=="oto"):
        if(echience <= 60):
            return True
        else:
            return capaciter_client*60   ### montant proposer
    elif(offre=="tanmiya"):
        if(echience <= 84):
            return True
        else:
            return capaciter_client*84   ### montant proposer
    elif(offre=="pie"):
        if(echience <= 48):
            return True
        else:
            return capaciter_client*48   ### montant proposer
    elif(offre=="pil"):
        if(echience <= 48):
            return True
        else:
            return capaciter_client*48   ### montant proposer


# Function to calculate the
# Jaro Similarity of two s
def jaro_distance(s1, s2):
     
    # If the s are equal
    if (s1 == s2):
        return 1.0
 
    # Length of two s
    len1 = len(s1)
    len2 = len(s2)
 
    # Maximum distance upto which matching
    # is allowed
    max_dist = floor(max(len1, len2) / 2) - 1
 
    # Count of matches
    match = 0
 
    # Hash for matches
    hash_s1 = [0] * len(s1)
    hash_s2 = [0] * len(s2)
 
    # Traverse through the first
    for i in range(len1):
 
        # Check if there is any matches
        for j in range(max(0, i - max_dist),
                       min(len2, i + max_dist + 1)):
             
            # If there is a match
            if (s1[i] == s2[j] and hash_s2[j] == 0):
                hash_s1[i] = 1
                hash_s2[j] = 1
                match += 1
                break
 
    # If there is no match
    if (match == 0):
        return 0.0
 
    # Number of transpositions
    t = 0
    point = 0
 
    # Count number of occurrences
    # where two characters match but
    # there is a third matched character
    # in between the indices
    for i in range(len1):
        if (hash_s1[i]):
 
            # Find the next matched character
            # in second
            while (hash_s2[point] == 0):
                point += 1
 
            if (s1[i] != s2[point]):
                t += 1
            point += 1
    t = t//2
 
    # Return the Jaro Similarity
    return (match/ len1 + match / len2 +
            (match - t) / match)/ 3.0
 
def split_adresse(adresse,k):

    i=1
    new_adresse=""
    for j in adresse:
        if(i==k and j==" "):
            new_adresse+="::"
            i=i+1
            continue
        elif(j==" "):
            i=i+1
            new_adresse+=j
        else:
            new_adresse+=j
    
    
    return(new_adresse.split("::",maxsplit=1))

def split_adresse_2(adresse):

    i=1
    new_adresse=""
    nmb=round(adresse.count(" ")/2)
    for j in adresse:
        if(i==nmb and j==" "):
            new_adresse+="::"
            i=i+1
            continue
        elif(j==" "):
            i=i+1
            new_adresse+=j
        else:
            new_adresse+=j
    
    
    return(new_adresse.split("::",maxsplit=1))
